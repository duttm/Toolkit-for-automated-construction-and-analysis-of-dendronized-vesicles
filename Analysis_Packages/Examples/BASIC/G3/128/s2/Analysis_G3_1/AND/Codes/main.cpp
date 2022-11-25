//// Compiling Instructions
//g++ -std=c++11 main.cpp
// this will generate an executable a.out
// run that using ./a.out


#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>
#include <vector>




// for DPPC


const int rows=36084;
const int frames =11;
const int netrows= rows*frames;




using namespace std;
double** reader(unsigned rows, unsigned cols, unsigned frames);
//double** reader_den( unsigned  rows_den, unsigned  cols_den, unsigned frames_den);

//double calculateSD(double aspect_ratio[],int p);


int main()


{
    string name1;
    
    // in the complete gro file, regardless of you taking a particular section
    string counter11, counter22, counter33, counter44;
    vector <string> v1;
    
    // This would be the standard procedure to generate a 2D blank array which can be passed
    
    
    ifstream filedppc_("/home/abanerjee/mantel/Jia/Analysis/DATA/G2/TESTING/onlyDPPC_G2_1_seed3.txt");
    
    int a_dppc=0;
    if (filedppc_.is_open())
    {
        while(!filedppc_.eof())
        {getline(filedppc_,name1, '\n');
            
            v1.push_back(name1);
            
            //            cout<<v1[a_dppc]<<endl;
            a_dppc++;
        }
    }
    else
    {
        cout<<"Can not read file"<<endl;
    }
    filedppc_.close();
    
    
    // Now we'll try to create a 3 by 5 "matrix".
    // First, create a vector with 5 elements
    vector<double> d3(4, 0);
    
    // Now create a vector of 3 elements.
    // Each element is a copy of v2
    vector<vector<double> > dump_data_dppc(netrows,d3);
    
    int iii=0;
    
    // the initial value of y will force quit the first 2 lines in the gro file and also the last 2
    
    int yh=2, y13=0, y23=0;
    while (y23< ( (netrows)) )
    {
        
        counter11=v1[yh].substr(0,5);
        counter22=v1[yh].substr(21,28); // Change counter values if needed
        counter33=v1[yh].substr(29,36);
        counter44=v1[yh].substr(37,44);
        
        dump_data_dppc[iii][0]=stod(counter11);
        dump_data_dppc[iii][1]=stod(counter22);
        dump_data_dppc[iii][2]=stod(counter33);
        dump_data_dppc[iii][3]=stod(counter44);
        
        
        iii++;
        y13++;
        yh++;
        y23++;
        
        
        if (y13== rows)
        { y13=0;
            yh=yh+3;
            
        }
        
    }
    
    
    /////-------
    
    // Terminate(Dump_data_display)
    
    // Lets find the center of the dataset ----- Begin(Center)
    
    
    // -------------Terminate(Center)----------
    
    // Convert 2d to 3d begin()-------
    //
    
    int g=0;
    
    vector<vector<vector<double> > > dump_three_DPPC; //declare the 3D vector
     vector<vector<vector<double> > > Outer_dump_three_DPPC; //declare the 3D vector
    vector<vector<vector<double> > > Inner_dump_three_DPPC; //declare the 3D vector
    for(int k=0; k<frames; k++)
    {
        dump_three_DPPC.push_back(vector<vector<double> >());
         Outer_dump_three_DPPC.push_back(vector<vector<double> >());
         Inner_dump_three_DPPC.push_back(vector<vector<double> >());
        
        for(int i=0; i<rows ; i++)
        {
            dump_three_DPPC[k].push_back(vector<double>());
              Outer_dump_three_DPPC[k].push_back(vector<double>());
            Inner_dump_three_DPPC[k].push_back(vector<double>());
            
            for(int j=0; j<5; j++)
            {
                
            dump_three_DPPC[k][i].push_back(0);
                Outer_dump_three_DPPC[k][i].push_back(0);
                  Inner_dump_three_DPPC[k][i].push_back(0);
                
                dump_three_DPPC[k][i][j]=dump_data_dppc[g][j];
                //                    cout<<dump_three_DPPC[k][i][j]<<" ";
                
            }
            g++;
            //                cout<<endl;
            
            
        }
        //            cout<<endl;
    }
    
 
    vector<double> c1(3, 0);
    vector<vector<double> > center(frames,c1);
    
    double  sum_col1_page=0, sum_col2_page=0, sum_col3_page=0, count_cols_page =0;
    
    
    for (int k=0; k<frames ; k++)
    { count_cols_page=0; sum_col1_page=0; sum_col2_page=0; sum_col3_page=0;
        
        for (int i=0; i<rows; i++)
        {
            sum_col1_page += dump_three_DPPC[k][i][1];
            sum_col2_page += dump_three_DPPC[k][i][2];
            sum_col3_page += dump_three_DPPC[k][i][3];
            
            count_cols_page++;
            
        }
        center[k][0]=sum_col1_page/count_cols_page;
        center[k][1]=sum_col2_page/count_cols_page;
        center[k][2]=sum_col3_page/count_cols_page;
        
//        cout<<"Center of frame "<<k+1<<" is "<<center[k][0]<<" "<<center[k][1]<<" "<<center[k][2]<<endl;
        
    }
    
    //    // Terminate Center of each page ---------
    //
    //    // Radius of Vesicle Framewise Calculation
    
    int count_dist=0;
    double dist=0;
    
    vector<double> c2(frames, 0);
    vector<vector<double> > store_dist(rows,c2);
    
    vector<double> avg_radius_GL(frames, 0);
    double outer_limiter=12; // This term excludes floating DPPC lipids which lie
    // outside the vesicle
    
    for (int k=0; k<frames ; k++)
    {
        for (int i=0; i<rows; i+=12 )
        {
            dist+= sqrt(   pow(( center[k][0]-dump_three_DPPC[k][i][1] ),2)+             pow( (center[k][1]-dump_three_DPPC[k][i][2]),2)
                        + pow( (center[k][2]-dump_three_DPPC[k][i][3]) ,2)   ) ;
            
            count_dist++;
            
            store_dist[i][k]=sqrt(   pow(( center[k][0]-dump_three_DPPC[k][i][1] ),2)+     pow( (center[k][1]-dump_three_DPPC[k][i][2])    ,2)
                                  + pow( (center[k][2]-dump_three_DPPC[k][i][3]) ,2)      ) ;
        
          
//            cout<<endl;
        }
        
        avg_radius_GL[k]=dist/count_dist;
        
        cout<<" Mean Radius of Vesicle for  Frame "<<k+1<<" is "<<avg_radius_GL[k]<<endl;
        dist=0; count_dist=0;
        
//        cout<<endl;
        
    }
    
    double upper_dist=0, lower_dist=0;
    int count_upper=0, count_lower=0;
    
    
    
    vector<double> mean_upper_dist(frames,0);
     vector<double> store_upper_count(frames,0);
    vector<double> mean_lower_dist(frames,0);
     vector<double> store_lower_count(frames,0);
    vector<double> Ain(frames,0);
    vector<double> Aout(frames,0);
    
    for (int k=0; k<frames ; k++)
    {
        for (int i=0; i<rows; i+=12 )
        {
            if (store_dist[i][k] > avg_radius_GL[k] && store_dist[i][k]<outer_limiter)
            {upper_dist += store_dist[i][k];
                count_upper++;
                
                
                for (int l=i; l<i+12; l++)
                {
                for (int j=0; j<4; j++)
                {
                    Outer_dump_three_DPPC[k][l][j]=dump_three_DPPC[k][l][j]; // Outer DPPC repositoty
                    
                }
                }
            }
            
            if (store_dist[i][k] <= avg_radius_GL[k]&& store_dist[i][k]<outer_limiter)
            {lower_dist += store_dist[i][k];
                count_lower++;
                
                for (int l=i; l<i+12; l++)
                {
                for (int j=0; j<4; j++)
                {
                    Inner_dump_three_DPPC[k][l][j]=dump_three_DPPC[k][l][j]; // Inner DPPC repositoty
                    
                }
                }
            }
            
        }
        mean_upper_dist[k]=upper_dist/count_upper;
        store_upper_count[k]=count_upper;
        Aout[k]= (4*3.14* (pow(mean_upper_dist[k],2)))/store_upper_count[k];
        
        mean_lower_dist[k]=lower_dist/count_lower;
        store_lower_count[k]=count_lower;
        Ain[k]= (4*3.14* (pow(mean_lower_dist[k],2)))/store_lower_count[k];
        
//        cout<<"Inner Monolayer are "<<count_lower<<" for frame "<<k+1<<endl;
//        cout<<"Outer Monolayer are "<<count_upper<<" for frame "<<k+1<<endl;
        
//        cout<<"Ro "<<mean_upper_dist[k]<<" Ri "<<mean_lower_dist[k]<<endl;
        
        upper_dist=0; lower_dist=0; count_upper=0; count_lower=0;
        
        
    }
    
    
//    for (int k=0; k<frames; k++)
//    {
//        for ( int i=0; i< rows; i++)
//        {
//            for (int j=0; j<4; j++)
//            {
//                cout<< Inner_dump_three_DPPC[k][i][j]<<" ";
//            }
//            cout<<endl;
//        }
//
//        cout<<endl;
//    }
    
    
//     Lets find COM for each frame of the outer lipids
    
    vector<double> o1(3, 0);
    vector<vector<double> > center_outer(frames,o1);
    
    double  outer_sum_col1_page=0, outer_sum_col2_page=0, outer_sum_col3_page=0, outer_count_cols_page =0;
    
    
    for (int k=0; k<frames ; k++)
    { outer_count_cols_page=0; outer_sum_col1_page=0; outer_sum_col2_page=0; outer_sum_col3_page=0;
        
        for (int i=0; i<rows; i++)
        { if (Outer_dump_three_DPPC[k][i][1] !=0)
        {   sum_col1_page += Outer_dump_three_DPPC[k][i][1];
            sum_col2_page += Outer_dump_three_DPPC[k][i][2];
            sum_col3_page += Outer_dump_three_DPPC[k][i][3];
            
            count_cols_page++;}
            
        }
        center_outer[k][0] =sum_col1_page/count_cols_page;
        center_outer[k][1] =sum_col2_page/count_cols_page;
        center_outer[k][2] =sum_col3_page/count_cols_page;
        
    }
    vector<double> o2(3, 0);
    vector<vector<double> > center_inner(frames,o2);
    
    double  inner_sum_col1_page=0, inner_sum_col2_page=0, inner_sum_col3_page=0, inner_count_cols_page =0;
    
    
    
    for (int k=0; k<frames ; k++)
    { inner_count_cols_page=0; inner_sum_col1_page=0; inner_sum_col2_page=0;
        inner_sum_col3_page=0;
        
        for (int i=0; i<rows; i++)
        { if (Inner_dump_three_DPPC[k][i][1] !=0)
        {  sum_col1_page += Inner_dump_three_DPPC[k][i][1];
            sum_col2_page += Inner_dump_three_DPPC[k][i][2];
            sum_col3_page += Inner_dump_three_DPPC[k][i][3];
            
            count_cols_page++;}
            
        }
        center_inner[k][0]=sum_col1_page/count_cols_page;
        center_inner[k][1]=sum_col2_page/count_cols_page;
        center_inner[k][2]=sum_col3_page/count_cols_page;
        
    }
//    for (int k=0; k<frames; k++)
//    {     cout<<"Center of inner in  frame "<<k+1<<" is "<<center_inner[k][0]<<" "<<center_inner[k][1]<<" "<<center_inner[k][2]<<endl;
//
//    cout<<"Center of outer in frame "<<k+1<<" is "<<center_outer[k][0]<<" "<<center_outer[k][1]<<" "<<center_outer[k][2]<<endl;
//    }
//
    // Lets find upper Lc
    vector<double> outer_volume(frames, 0);
    vector<double> outer_lc(frames, 0);
    vector<double> o3(frames, 0);
    vector<vector<double> > store_outer_tail_dist(rows,o3);
    
    int z=0, z1=0; // pointer
    double temp=0;
    
    for (int k=0; k < frames; k++)
         {
             for (int l=2; l<rows; l+=12)
             {
             for (int i=l; i< l+10; i++)
             {
                 if (Outer_dump_three_DPPC[k][l][1] !=0)
                     
                 {
                     Outer_dump_three_DPPC[k][i][4]=sqrt(   pow(( center_outer[k][0]-Outer_dump_three_DPPC[k][i][1] ),2)
                        +             pow( (center_outer[k][1]-Outer_dump_three_DPPC[k][i][2]),2)
                            + pow( (center_outer[k][2]-Outer_dump_three_DPPC[k][i][3]) ,2)   ) ;
                     
//                     cout<<Outer_dump_three_DPPC[k][i][0]<<" "<<Outer_dump_three_DPPC[k][i][1]
//                     <<" "<<Outer_dump_three_DPPC[k][i][2]<<" "<<Outer_dump_three_DPPC[k][i][3]
//                     <<" "<<Outer_dump_three_DPPC[k][i][4]<<" ";
//
                     store_outer_tail_dist[z][k]= Outer_dump_three_DPPC[k][i][4];
//                     cout<<store_outer_tail_dist[z][k]<<endl;
                     z++; z1++;
                 }
//                 cout<<endl;
                 
             }
//             cout<<endl;
             }
             
             for(int a=0;a<z;a++)
             {
                 for(int b=a+1;b<z;b++)
                 {
                     if( store_outer_tail_dist[a][k]> store_outer_tail_dist[b][k])
                     {
                         temp  = store_outer_tail_dist[a][k];
                          store_outer_tail_dist[a][k]=store_outer_tail_dist[b][k];
                        store_outer_tail_dist[b][k]=temp;
                     }
                 }
             }
             
             double outer_sum_top=0, outer_sum_bottom=0;
             for (int a=0; a< 2*store_upper_count[k]; a++)
             {
                 outer_sum_top += store_outer_tail_dist[a][k];
                 outer_sum_bottom +=store_outer_tail_dist[z-1-a][k];
             }
             outer_sum_top=outer_sum_top/(2*store_upper_count[k]);
             outer_sum_bottom=outer_sum_bottom/(2*store_upper_count[k]);
//             cout<< outer_sum_bottom-outer_sum_top<<endl;
             outer_lc[k]=outer_sum_bottom-outer_sum_top;
              outer_volume[k]= ((4/3)*(3.14)* ( pow(outer_sum_bottom,3) - pow(outer_sum_top,3)  ))/store_upper_count[k];
             z=0;
         }
    
    // Lets find Inner Lc
    vector<double> inner_volume(frames, 0);
    vector<double> inner_lc(frames, 0);
    vector<double> o4(frames, 0);
    vector<vector<double> > store_inner_tail_dist(rows,o4);
    
    int z2=0, z3=0; // pointer
    double temp1=0;
    
    for (int k=0; k < frames; k++)
    {
        for (int l=2; l<rows; l+=12)
        {
            for (int i=l; i< l+10; i++)
            {
                if (Inner_dump_three_DPPC[k][l][1] !=0)
                    
                {
                    Inner_dump_three_DPPC[k][i][4]=sqrt(   pow(( center_inner[k][0]-Inner_dump_three_DPPC[k][i][1] ),2)
                                                        +             pow( (center_inner[k][1]-Inner_dump_three_DPPC[k][i][2]),2)
                                                        + pow( (center_inner[k][2]-Inner_dump_three_DPPC[k][i][3]) ,2)   ) ;
                    
                  
                    store_inner_tail_dist[z2][k]= Inner_dump_three_DPPC[k][i][4];
//                                         cout<<store_outer_tail_dist[z2][k]<<endl;
                    z2++; z3++;
                }
//                                 cout<<endl;
                
            }
//                         cout<<endl;
        }
        
        for(int a=0;a<z2;a++)
        {
            for(int b=a+1;b<z2;b++)
            {
                if( store_inner_tail_dist[a][k]> store_inner_tail_dist[b][k])
                {
                    temp1  = store_inner_tail_dist[a][k];
                    store_inner_tail_dist[a][k]=store_inner_tail_dist[b][k];
                    store_inner_tail_dist[b][k]=temp1;
                }
            }
        }
        
        double inner_sum_top=0, inner_sum_bottom=0;
        
        for (int a=0; a< 2*store_lower_count[k]; a++)
        {
            inner_sum_top += store_inner_tail_dist[a][k];
            inner_sum_bottom +=store_inner_tail_dist[z2-1-a][k];
        }
        inner_sum_top=inner_sum_top/(2*store_lower_count[k]);
        inner_sum_bottom=inner_sum_bottom/(2*store_lower_count[k]);
//                     cout<< inner_sum_bottom-inner_sum_top<<endl;
        inner_lc[k]=inner_sum_bottom-inner_sum_top;
        inner_volume[k]= ((4/3)*(3.14)* ( pow(inner_sum_bottom,3) - pow(inner_sum_top,3)  ))/store_lower_count[k];
        z2=0;
    }
    
    double inner_lc_mean=0, outer_lc_mean=0, inner_volume_mean=0, outer_volume_mean=0, mean_outer_radius=0, mean_lower_radius=0, mean_Ain=0, mean_Aout=0, mean_packing_factor_inner=0, mean_packing_factor_outer=0, mean_hydro_thick=0;

    for (int i=0; i< frames; i++)

    {
//        cout<<inner_lc[i]<<endl;
//        cout<<outer_lc[i]<<endl;
        inner_lc_mean+=inner_lc[i];
        outer_lc_mean+=outer_lc[i];
        inner_volume_mean+=inner_volume[i];
        outer_volume_mean+=outer_volume[i];
        mean_outer_radius+=mean_upper_dist[i];
        mean_lower_radius+=mean_lower_dist[i];
        mean_hydro_thick+= (mean_upper_dist[i]-mean_lower_dist[i]);
        mean_Ain+=Ain[i];
        mean_Aout+=Aout[i];
        mean_packing_factor_inner+= (inner_volume[i])/(Ain[i]*inner_lc[i]);
        mean_packing_factor_outer+= (outer_volume[i])/(Aout[i]*outer_lc[i]);
    }
    
    inner_lc_mean=inner_lc_mean/frames;
    outer_lc_mean=outer_lc_mean/frames;
    inner_volume_mean=inner_volume_mean/frames;
    outer_volume_mean=outer_volume_mean/frames;
    mean_outer_radius=mean_outer_radius/frames;
    mean_lower_radius=mean_lower_radius/frames;
    mean_hydro_thick=mean_hydro_thick/frames;
    mean_Aout=mean_Aout/frames;
    mean_Ain=mean_Ain/frames;
    mean_packing_factor_inner=mean_packing_factor_inner/frames;
    mean_packing_factor_outer=mean_packing_factor_outer/frames;
    

   
    // Yet to add stdevs 
    
    
    double  standardDeviation_innervolume = 0,  standardDeviation_outervolume = 0, standardDeviation_Ri = 0 , standardDeviation_Ro=0, standardDeviation_Ain=0,
    standardDeviation_Aout=0, standardDeviation_pack_in=0, standardDeviation_pack_out=0,
    standardDeviation_hydrothick=0, standardDeviation_lc_inner=0, standardDeviation_lc_outer=0;
    
    for(int i = 0; i < frames; ++i)
    { standardDeviation_innervolume += pow(inner_volume[i] - inner_volume_mean, 2);
        standardDeviation_outervolume += pow(outer_volume[i] - outer_volume_mean, 2);
        standardDeviation_Ri += pow(mean_lower_dist[i] - mean_lower_radius, 2);
        standardDeviation_Ro += pow(mean_upper_dist[i] - mean_outer_radius, 2);
        standardDeviation_Ain += pow(Ain[i] - mean_Ain, 2);
        standardDeviation_Aout += pow(Aout[i] - mean_Aout, 2);
        standardDeviation_pack_in += pow( ((inner_volume[i])/(Ain[i]*inner_lc[i])) - mean_packing_factor_inner, 2);
        standardDeviation_pack_out += pow( ((outer_volume[i])/(Aout[i]*outer_lc[i])) - mean_packing_factor_outer, 2);
        
        standardDeviation_hydrothick += pow( ((mean_upper_dist[i]-mean_lower_dist[i]))    - mean_hydro_thick, 2);
        
        standardDeviation_lc_inner += pow(  inner_lc[i]   - inner_lc_mean, 2);
          standardDeviation_lc_outer += pow(  outer_lc[i]   - outer_lc_mean, 2);
        
        
    }
    
    double std_innervolume=0, std_outervolume=0, std_Ri=0 , std_Ro=0, std_Ain=0,
    std_Aout=0, std_pack_in=0, std_pack_out=0,
    std_hydrothick=0, std_lc_inner=0, std_lc_outer=0;
    
    
    std_innervolume= sqrt(standardDeviation_innervolume / frames);
    std_outervolume= sqrt(standardDeviation_outervolume / frames);
    std_Ri= sqrt(standardDeviation_Ri/ frames);
    std_Ro= sqrt(standardDeviation_Ro/ frames);
    std_Ain= sqrt(standardDeviation_Ain/ frames);
    std_Aout= sqrt(standardDeviation_Aout/ frames);
    std_pack_in= sqrt(standardDeviation_pack_in/ frames);
    std_pack_out= sqrt(standardDeviation_pack_out/ frames);
    std_hydrothick= sqrt(standardDeviation_hydrothick/ frames);
    std_lc_inner= sqrt(standardDeviation_lc_inner/ frames);
    std_lc_outer= sqrt(standardDeviation_lc_outer/ frames);
    
    cout<<" ------------------------------------------"<<endl;
    cout<<"Inner_lc "<<inner_lc_mean<<" "<<std_lc_inner<<endl;
    cout<<"Outer_lc "<<outer_lc_mean<<" "<<std_lc_outer<<endl;
    cout<<"Inner_Volume "<<inner_volume_mean<<" "<<std_innervolume<<endl;
    cout<<"Outer_Volume "<<outer_volume_mean<<" "<<std_outervolume<<endl;
    cout<<"Ri "<<mean_lower_radius<<" "<<std_Ri<<endl;
    cout<<"Ro "<<mean_outer_radius<<" "<<std_Ro<<endl;
    cout<<"Ain "<<mean_Ain<<" "<<std_Ain<<endl;
    cout<<"Aout "<<mean_Aout<<" "<<std_Aout<<endl;
    cout<<"Pack_factor_inner "<<mean_packing_factor_inner<<" "<<std_pack_in<<endl;
    cout<<"Pack_factor_outer "<<mean_packing_factor_outer<<" "<<std_pack_out<<endl;
    cout<<"Hydrophilic_thickness "<<mean_hydro_thick<<" "<<std_hydrothick<<endl;
     cout<<" ------------------------------------------"<<endl;
    
    return 0;
    
}

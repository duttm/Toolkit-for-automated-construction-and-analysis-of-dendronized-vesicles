#!/usr/bin/gnuplot
# looks ok with gnuplot 5.2


reset

set output 'DEN_Layer_Thickness_G2_G4_G6.png'

set term post portrait enhanced color 

set terminal pngcairo  enhanced font "Times New Roman,12" fontscale 1.0 size 700, 350

# 1 rows and 2 columns
##set multiplot layout 1,2

set border linewidth 1
set tics nomirror
set xtics 2
set ytics 0.5

# if tics don't do it for you then you can comment above and uncomment this one
# unset tics


set xlabel "Number of Dendrons" font "Times-New-Roman,12" offset -1,0.5 

set ylabel "Thickness (nm)" font "Times-New-Roman,12" offset 1.5,0.6
                


set xzeroaxis linetype -1 linewidth 1

set logscale x 2
set tics nomirror
set xrange [4:1000]
set yrange [0.0:3.0]

set style line 1 \
    linecolor rgb 'black' \
    linetype 1 linewidth 1 \
    pointtype 7 pointsize 1
    
set style line 2 \
    linecolor rgb 'black' \
    linetype 1 linewidth 1 \
    dashtype "-" \
    pointtype 9 pointsize 1
    
set style line 3 \
    linecolor rgb 'red' \
    linetype 1 linewidth 1 \
    pointtype 7 pointsize 1
    
set style line 4 \
    linecolor rgb 'red' \
    linetype 1 linewidth 1 \
    dashtype "-" \
    pointtype 9 pointsize 1
    
set style line 5 \
    linecolor rgb 'blue' \
    linetype 1 linewidth 1 \
    pointtype 7 pointsize 1
    
set style line 6 \
    linecolor rgb 'blue' \
    linetype 1 linewidth 1 \
    dashtype "-" \
    pointtype 9 pointsize 1
    
set key left bottom
    
    

##set label 1 '(A)' at graph -0.18,0.85 font "Times-New-Roman,12"
plot '../DATA/ACIDIC/Den_layer_thickness/SummaryG2.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "black" linewidth 3 not,\
 '../DATA/ACIDIC/Den_layer_thickness/SummaryG2.txt'  using  ($2):($3) with linespoints linestyle 1 title "G2-Acidic" ,\
 '../DATA/BASIC/Den_layer_thickness/SummaryG2.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "black" linewidth 3 not,\
 '../DATA/BASIC/Den_layer_thickness/SummaryG2.txt'  using  2:($3) with linespoints linestyle 2 title "G2-Basic", \
  '../DATA/ACIDIC/Den_layer_thickness/SummaryG4.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "red" linewidth 3 not,\
 '../DATA/ACIDIC/Den_layer_thickness/SummaryG4.txt'  using  ($2):($3) with linespoints linestyle 3 title "G4-Acidic" ,\
 '../DATA/BASIC/Den_layer_thickness/SummaryG4.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "red" linewidth 3 not,\
 '../DATA/BASIC/Den_layer_thickness/SummaryG4.txt'  using  2:($3) with linespoints linestyle 4 title "G4-Basic", \
  '../DATA/ACIDIC/Den_layer_thickness/SummaryG6.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "blue" linewidth 3 not,\
 '../DATA/ACIDIC/Den_layer_thickness/SummaryG6.txt'  using  ($2):($3) with linespoints linestyle 5 title "G6-Acidic" ,\
 '../DATA/BASIC/Den_layer_thickness/SummaryG6.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "blue" linewidth 3 not,\
 '../DATA/BASIC/Den_layer_thickness/SummaryG6.txt'  using  2:($3) with linespoints linestyle 6 title "G6-Basic", \
##with lines title "Runtime(Seconds)" lt rgb "black" linewidth 2

unset multiplot

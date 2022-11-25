#!/usr/bin/gnuplot
# looks ok with gnuplot 5.2


reset

filename = "ROGvsAND"
ph1= "ACIDIC"
ph2 = "BASIC"


yaxis = "Measurement"

set output filename.'_all_conc.png'

set term post portrait enhanced color 

set terminal pngcairo  enhanced font "Times New Roman,12" fontscale 1.0 size 800, 1000

# 1 rows and 2 columns
set multiplot layout 5,2

set border linewidth 1
set tics nomirror
set xtics 2
set ytics 5

# if tics don't do it for you then you can comment above and uncomment this one
# unset tics




set xlabel "Conc of Dens" font "Times-New-Roman,12" offset -1,0.5 

set ylabel yaxis font "Times-New-Roman,12" offset 1.5,0.6
                


set xzeroaxis linetype -1 linewidth 1

set logscale x 2
set tics nomirror
set xrange [1:100]
set yrange [0:10.0]

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
    
set style line 7 \
    linecolor rgb '#005A32' \
    linetype 1 linewidth 1 \
    pointtype 7 pointsize 1
    
set style line 8 \
    linecolor rgb '#005A32' \
    linetype 1 linewidth 1 \
    dashtype "-" \
    pointtype 9 pointsize 1
    
set style line 9 \
    linecolor rgb 'violet' \
    linetype 1 linewidth 1 \
    pointtype 7 pointsize 1
    
set style line 10 \
    linecolor rgb 'violet' \
    linetype 1 linewidth 1 \
    dashtype "-" \
    pointtype 9 pointsize 1
    
set style line 11 \
    linecolor rgb 'orange' \
    linetype 1 linewidth 1 \
    pointtype 7 pointsize 1
    
set style line 12 \
    linecolor rgb 'orange' \
    linetype 1 linewidth 1 \
    dashtype "-" \
    pointtype 9 pointsize 1
    
    
set key right top
    
Mw=72    
gen=1
a=(8*(2**(gen-1))-1)*Mw        
    

set label 1 '(A)' at graph -0.08,0.85 font "Times-New-Roman,12"

plot '../../DATA/'.ph1.'/'.filename.'/SummaryG1.txt'  using  (($2*100)/3039):(2*$5) with linespoints linestyle 1 title "G1-2ROG" ,\
 '../../DATA/'.ph1.'/'.filename.'/SummaryG1.txt'  using  (($2*100)/3039):($3) with linespoints linestyle 2 title "G1-AND", \


set label 1 '(B)'

plot '../../DATA/'.ph2.'/'.filename.'/SummaryG1.txt'  using  (($2*100)/3039):(2*$5) with linespoints linestyle 1 title "G1-2ROG" ,\
 '../../DATA/'.ph2.'/'.filename.'/SummaryG1.txt'  using  (($2*100)/3039):($3) with linespoints linestyle 2 title "G1-AND", \
 


gen=2
a=(8*(2**(gen-1))-1)*Mw        
    

set label 1 '(C)' 

plot '../../DATA/'.ph1.'/'.filename.'/SummaryG2.txt'  using  (($2*100)/3039):(2*$5) with linespoints linestyle 3 title "G2-2ROG" ,\
 '../../DATA/'.ph1.'/'.filename.'/SummaryG2.txt'  using  (($2*100)/3039):($3) with linespoints linestyle 4 title "G2-AND", \


set label 1 '(D)'

plot '../../DATA/'.ph2.'/'.filename.'/SummaryG2.txt'  using  (($2*100)/3039):(2*$5) with linespoints linestyle 3 title "G2-2ROG" ,\
 '../../DATA/'.ph2.'/'.filename.'/SummaryG2.txt'  using  (($2*100)/3039):($3) with linespoints linestyle 4 title "G2-AND", \
 

gen=3
a=(8*(2**(gen-1))-1)*Mw        
    

set label 1 '(E)' 

plot '../../DATA/'.ph1.'/'.filename.'/SummaryG3.txt'  using  (($2*100)/3039):(2*$5) with linespoints linestyle 5 title "G3-2ROG" ,\
 '../../DATA/'.ph1.'/'.filename.'/SummaryG3.txt'  using  (($2*100)/3039):($3) with linespoints linestyle 6 title "G3-AND", \


set label 1 '(F)'

plot '../../DATA/'.ph2.'/'.filename.'/SummaryG3.txt'  using  (($2*100)/3039):(2*$5) with linespoints linestyle 5 title "G3-2ROG" ,\
 '../../DATA/'.ph2.'/'.filename.'/SummaryG3.txt'  using  (($2*100)/3039):($3) with linespoints linestyle 6 title "G3-AND", \
 
gen=4
a=(8*(2**(gen-1))-1)*Mw        
    

set label 1 '(G)' 

plot '../../DATA/'.ph1.'/'.filename.'/SummaryG4.txt'  using  (($2*100)/3039):(2*$5) with linespoints linestyle 7 title "G4-2ROG" ,\
 '../../DATA/'.ph1.'/'.filename.'/SummaryG4.txt'  using  (($2*100)/3039):($3) with linespoints linestyle 8 title "G4-AND", \


set label 1 '(H)'

plot '../../DATA/'.ph2.'/'.filename.'/SummaryG4.txt'  using  (($2*100)/3039):(2*$5) with linespoints linestyle 7 title "G4-2ROG" ,\
 '../../DATA/'.ph2.'/'.filename.'/SummaryG4.txt'  using  (($2*100)/3039):($3) with linespoints linestyle 8 title "G4-AND", \
 

gen=5
a=(8*(2**(gen-1))-1)*Mw        
    

set label 1 '(I)' 

plot '../../DATA/'.ph1.'/'.filename.'/SummaryG5.txt'  using  (($2*100)/3039):(2*$5) with linespoints linestyle 9 title "G5-2ROG" ,\
 '../../DATA/'.ph1.'/'.filename.'/SummaryG5.txt'  using  (($2*100)/3039):($3) with linespoints linestyle 10 title "G5-AND", \


set label 1 '(J)'

plot '../../DATA/'.ph2.'/'.filename.'/SummaryG5.txt'  using  (($2*100)/3039):(2*$5) with linespoints linestyle 9 title "G5-2ROG" ,\
 '../../DATA/'.ph2.'/'.filename.'/SummaryG5.txt'  using  (($2*100)/3039):($3) with linespoints linestyle 10 title "G5-AND", \
 




  ##'../DATA/ACIDIC/'.filename.'/SummaryG6.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "orange" linewidth 3 not,\
 ##'../DATA/ACIDIC/'.filename.'/SummaryG6.txt'  using  ($2):($3) with linespoints linestyle 11 title "G6-Acidic" ,\
 ##'../DATA/BASIC/'.filename.'/SummaryG6.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "orange" linewidth 3 not,\
 ##'../DATA/BASIC/'.filename.'/SummaryG6.txt'  using  2:($3) with linespoints linestyle 12 title "G6-Basic", \

##with lines title "Runtime(Seconds)" lt rgb "black" linewidth 2

unset multiplot

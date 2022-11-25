#!/usr/bin/gnuplot
# looks ok with gnuplot 5.2


reset

filename = "DHS_TAbeads"

yaxis = "Frac surface area covered"

set output filename.'_all_split_Mw.png'

set term post portrait enhanced color 

set terminal pngcairo  enhanced font "Times New Roman,12" fontscale 1.0 size 900, 500

# 1 rows and 2 columns
set multiplot layout 1,2

set border linewidth 1
set tics nomirror
set xtics 4
set ytics 0.2

# if tics don't do it for you then you can comment above and uncomment this one
# unset tics




set xlabel "Mw of Dendrons" font "Times-New-Roman,12" offset -1,0.5 

set ylabel yaxis font "Times-New-Roman,12" offset 1.5,0.6
                


set xzeroaxis linetype -1 linewidth 1


set logscale x 2
set tics nomirror
set xrange [8000:3000000]
set yrange [0.0:1.0]

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
    linecolor rgb 'green' \
    linetype 1 linewidth 1 \
    pointtype 7 pointsize 1
    
set style line 8 \
    linecolor rgb 'green' \
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
    
    
set key left top


Mw=72    
gen=1
a1=(8*(2**(gen-1))-1)*Mw    


gen=2
a2=(8*(2**(gen-1))-1)*Mw  

gen=3
a3=(8*(2**(gen-1))-1)*Mw  

gen=4
a4=(8*(2**(gen-1))-1)*Mw  

gen=5
a5=(8*(2**(gen-1))-1)*Mw    

set label 1 '(A)' at graph -0.08,0.85 font "Times-New-Roman,12"

plot '../../DATA/ACIDIC/'.filename.'/SummaryG1.txt'  using  (a1*$2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "black" linewidth 3 not,\
 '../../DATA/ACIDIC/'.filename.'/SummaryG1.txt'  using  (a1*$2):($3) with linespoints linestyle 1 title "G1-Acidic" ,\
 '../../DATA/ACIDIC/'.filename.'/SummaryG2.txt'  using  (a2*$2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "green" linewidth 3 not,\
 '../../DATA/ACIDIC/'.filename.'/SummaryG2.txt'  using  (a2*$2):($3) with linespoints linestyle 7 title "G2-Acidic" ,\
 '../../DATA/ACIDIC/'.filename.'/SummaryG3.txt'  using  (a3*$2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "red" linewidth 3 not,\
 '../../DATA/ACIDIC/'.filename.'/SummaryG3.txt'  using  (a3*$2):($3) with linespoints linestyle 3 title "G3-Acidic" ,\
 '../../DATA/ACIDIC/'.filename.'/SummaryG4.txt'  using  (a4*$2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "violet" linewidth 3 not,\
 '../../DATA/ACIDIC/'.filename.'/SummaryG4.txt'  using  (a4*$2):($3) with linespoints linestyle 9 title "G4-Acidic" ,\
  '../../DATA/ACIDIC/'.filename.'/SummaryG5.txt'  using  (a5*$2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "blue" linewidth 3 not,\
 '../../DATA/ACIDIC/'.filename.'/SummaryG5.txt'  using  (a5*$2):($3) with linespoints linestyle 5 title "G5-Acidic" ,\

set label 1 '(B)' 


plot '../../DATA/BASIC/'.filename.'/SummaryG1.txt'  using  (a1*$2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "black" linewidth 3 not,\
 '../../DATA/BASIC/'.filename.'/SummaryG1.txt'  using  (a1*$2):($3) with linespoints linestyle 2 title "G1-Basic", \
 '../../DATA/BASIC/'.filename.'/SummaryG2.txt'  using  (a2*$2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "green" linewidth 3 not,\
 '../../DATA/BASIC/'.filename.'/SummaryG2.txt'  using  (a2*$2):($3) with linespoints linestyle 8 title "G2-Basic", \
 '../../DATA/BASIC/'.filename.'/SummaryG3.txt'  using  (a3*$2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "red" linewidth 3 not,\
 '../../DATA/BASIC/'.filename.'/SummaryG3.txt'  using  (a3*$2):($3) with linespoints linestyle 4 title "G3-Basic", \
  '../../DATA/BASIC/'.filename.'/SummaryG4.txt'  using  (a4*$2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "violet" linewidth 3 not,\
 '../../DATA/BASIC/'.filename.'/SummaryG4.txt'  using  (a4*$2):($3) with linespoints linestyle 10 title "G4-Basic", \
 '../../DATA/BASIC/'.filename.'/SummaryG5.txt'  using  (a5*$2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "blue" linewidth 3 not,\
 '../../DATA/BASIC/'.filename.'/SummaryG5.txt'  using  (a5*$2):($3) with linespoints linestyle 6 title "G5-Basic", \


unset multiplot

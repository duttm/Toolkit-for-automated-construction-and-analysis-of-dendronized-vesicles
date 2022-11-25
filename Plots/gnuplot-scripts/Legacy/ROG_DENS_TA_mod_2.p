#!/usr/bin/gnuplot
# looks ok with gnuplot 5.2


reset

filename = "ROG_DENS_TA"

yaxis = "ROG(nm)"

set output filename.'_G1_G3_G5.png'

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

set ylabel yaxis font "Times-New-Roman,12" offset 1.5,0.6
                


set xzeroaxis linetype -1 linewidth 1

set logscale x 2
set tics nomirror
set xrange [16:3000]
set yrange [0.7:3.0]

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
##set label 1 '(A)' at graph -0.18,0.85 font "Times-New-Roman,12"

plot '../DATA/ACIDIC/'.filename.'/SummaryG1.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "black" linewidth 3 not,\
 '../DATA/ACIDIC/'.filename.'/SummaryG1.txt'  using  ($2):($3) with linespoints linestyle 1 title "G1-Acidic" ,\
 '../DATA/BASIC/'.filename.'/SummaryG1.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "black" linewidth 3 not,\
 '../DATA/BASIC/'.filename.'/SummaryG1.txt'  using  2:($3) with linespoints linestyle 2 title "G1-Basic", \
  '../DATA/ACIDIC/'.filename.'/SummaryG3.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "red" linewidth 3 not,\
 '../DATA/ACIDIC/'.filename.'/SummaryG3.txt'  using  ($2):($3) with linespoints linestyle 3 title "G3-Acidic" ,\
 '../DATA/BASIC/'.filename.'/SummaryG3.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "red" linewidth 3 not,\
 '../DATA/BASIC/'.filename.'/SummaryG3.txt'  using  2:($3) with linespoints linestyle 4 title "G3-Basic", \
  '../DATA/ACIDIC/'.filename.'/SummaryG5.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "blue" linewidth 3 not,\
 '../DATA/ACIDIC/'.filename.'/SummaryG5.txt'  using  ($2):($3) with linespoints linestyle 5 title "G5-Acidic" ,\
 '../DATA/BASIC/'.filename.'/SummaryG5.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "blue" linewidth 3 not,\
 '../DATA/BASIC/'.filename.'/SummaryG5.txt'  using  2:($3) with linespoints linestyle 6 title "G5-Basic", \


  ##'../DATA/ACIDIC/'.filename.'/SummaryG6.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "orange" linewidth 3 not,\
 ##'../DATA/ACIDIC/'.filename.'/SummaryG6.txt'  using  ($2):($3) with linespoints linestyle 11 title "G6-Acidic" ,\
 ##'../DATA/BASIC/'.filename.'/SummaryG6.txt'  using  ($2):($3):($4) with yerrorbars ls 7 ps 0.1 lt rgb "orange" linewidth 3 not,\
 ##'../DATA/BASIC/'.filename.'/SummaryG6.txt'  using  2:($3) with linespoints linestyle 12 title "G6-Basic", \



unset multiplot

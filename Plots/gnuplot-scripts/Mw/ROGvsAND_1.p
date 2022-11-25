#!/usr/bin/gnuplot
# looks ok with gnuplot 5.2


reset

filename = "ROGvsAND"
ph= "ACIDIC"

yaxis = "Measurement"

set output filename.ph.'_all.png'

set encoding iso_8859_1
set term postscript eps enhanced color

set terminal pngcairo  enhanced font "Times New Roman,14" fontscale 1.0 size 800, 850

# 1 rows and 2 columns
set multiplot layout 2,1

set border linewidth 1
set tics nomirror
set xtics 10
set ytics 2

# if tics don't do it for you then you can comment above and uncomment this one
# unset tics




set xlabel "Molecular Weight of Dendrons" font "Times-New-Roman,16" offset -1,0.5 

set ylabel yaxis font "Times-New-Roman,16" offset 1.5,0.6
                


set xzeroaxis linetype -1 linewidth 1

set logscale x 2
set tics nomirror
set xrange [8000:3000000]
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
      
##set key left top

set key at graph 0.22, 1
set label 1 '(A)' at graph -0.08,0.85 font "Times-New-Roman,14"

plot '../../DATA/'.ph.'/'.filename.'/SummaryG1.txt'  using  (a1*$2):(2*$5) with linespoints linestyle 1 title "G1-2{\327}R_G" ,\
 '../../DATA/'.ph.'/'.filename.'/SummaryG1.txt'  using  (a1*$2):($3) with linespoints linestyle 2 title "G1-AND", \
 '../../DATA/'.ph.'/'.filename.'/SummaryG2.txt'  using  (a2*$2):(2*$5) with linespoints linestyle 3 title "G2-2{\327}R_G" ,\
 '../../DATA/'.ph.'/'.filename.'/SummaryG2.txt'  using  (a2*$2):($3) with linespoints linestyle 4 title "G2-AND", \
 '../../DATA/'.ph.'/'.filename.'/SummaryG3.txt'  using  (a3*$2):(2*$5) with linespoints linestyle 5 title "G3-2{\327}R_G" ,\
 '../../DATA/'.ph.'/'.filename.'/SummaryG3.txt'  using  (a3*$2):($3) with linespoints linestyle 6 title "G3-AND", \
 '../../DATA/'.ph.'/'.filename.'/SummaryG4.txt'  using  (a4*$2):(2*$5) with linespoints linestyle 7 title "G4-2{\327}R_G" ,\
 '../../DATA/'.ph.'/'.filename.'/SummaryG4.txt'  using  (a4*$2):($3) with linespoints linestyle 8 title "G4-AND", \
 '../../DATA/'.ph.'/'.filename.'/SummaryG5.txt'  using  (a5*$2):(2*$5) with linespoints linestyle 9 title "G5-2{\327}R_G" ,\
 '../../DATA/'.ph.'/'.filename.'/SummaryG5.txt'  using  (a5*$2):($3) with linespoints linestyle 10 title "G5-AND", \

ph= "BASIC"

set label 1 '(B)' 

plot '../../DATA/'.ph.'/'.filename.'/SummaryG1.txt'  using  (a1*$2):(2*$5) with linespoints linestyle 1 title "G1-2{\327}R_G" ,\
 '../../DATA/'.ph.'/'.filename.'/SummaryG1.txt'  using  (a1*$2):($3) with linespoints linestyle 2 title "G1-AND", \
 '../../DATA/'.ph.'/'.filename.'/SummaryG2.txt'  using  (a2*$2):(2*$5) with linespoints linestyle 3 title "G2-2{\327}R_G" ,\
 '../../DATA/'.ph.'/'.filename.'/SummaryG2.txt'  using  (a2*$2):($3) with linespoints linestyle 4 title "G2-AND", \
 '../../DATA/'.ph.'/'.filename.'/SummaryG3.txt'  using  (a3*$2):(2*$5) with linespoints linestyle 5 title "G3-2{\327}R_G" ,\
 '../../DATA/'.ph.'/'.filename.'/SummaryG3.txt'  using  (a3*$2):($3) with linespoints linestyle 6 title "G3-AND", \
 '../../DATA/'.ph.'/'.filename.'/SummaryG4.txt'  using  (a4*$2):(2*$5) with linespoints linestyle 7 title "G4-2{\327}R_G" ,\
 '../../DATA/'.ph.'/'.filename.'/SummaryG4.txt'  using  (a4*$2):($3) with linespoints linestyle 8 title "G4-AND", \
 '../../DATA/'.ph.'/'.filename.'/SummaryG5.txt'  using  (a5*$2):(2*$5) with linespoints linestyle 9 title "G5-2{\327}R_G" ,\
 '../../DATA/'.ph.'/'.filename.'/SummaryG5.txt'  using  (a5*$2):($3) with linespoints linestyle 10 title "G5-AND", \






unset multiplot

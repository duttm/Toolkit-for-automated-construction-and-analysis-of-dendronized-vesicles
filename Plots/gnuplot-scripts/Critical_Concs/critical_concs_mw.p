#!/usr/bin/gnuplot
# looks ok with gnuplot 5.2


reset

filename = "Critical_Concs"

yaxis = "Generation"

set output filename.'_all_gens_mw.png'

set term post portrait enhanced color 

set terminal pngcairo  enhanced font "Times New Roman,12" fontscale 1.0 size 700, 350

# 1 rows and 2 columns
##set multiplot layout 1,2

set border linewidth 1
set tics nomirror
set xtics 2
set ytics 1

# if tics don't do it for you then you can comment above and uncomment this one
# unset tics




set xlabel "Mw of Dendrons" font "Times-New-Roman,12" offset -1,0.5 

set ylabel yaxis font "Times-New-Roman,12" offset 1.5,0.6
                




set xzeroaxis linetype -1 linewidth 1

set logscale x 2
set tics nomirror
STATS_max = 3000000
##set xrange [300000:100*ceil(STATS_max/100.0)]
set xrange [300000:STATS_max]
set yrange [0:5]

set style line 1 \
    linecolor rgb 'black' \
    dashtype "-" \
    linetype 1 linewidth 1 \
    pointtype 7 pointsize 1
    

    
set style line 3 \
    linecolor rgb 'red' \
    dashtype "-" \
    linetype 1 linewidth 1 \
    pointtype 7 pointsize 1
    

    
set style line 5 \
    linecolor rgb 'blue' \
    dashtype "-" \
    linetype 1 linewidth 1 \
    pointtype 7 pointsize 1
    
set style line 6 \
    linecolor rgb 'blue' \
    linetype 1 linewidth 1 \
    dashtype "-" \
    pointtype 7 pointsize 1

    
    
set key right top
##set label 1 '(A)' at graph -0.18,0.85 font "Times-New-Roman,12"
plot 'critical_concs_mw.txt'  using  ($2):($1) with linespoints linestyle 1 title "Acidic",  'critical_concs_mw.txt'  using  ($3):($1) with linespoints linestyle 5 title "Basic"
 
##plot 'critical_concs_mw.txt'  using  ($2):($1) with linespoints linestyle 1 title "Acidic", 'critical_concs_mw.txt'  using  ($4):($1) with ##linespoints linestyle 3 title "Neutral", 'critical_concs_mw.txt'  using  ($3):($1) with linespoints linestyle 5 title "Basic"
 



##with lines title "Runtime(Seconds)" lt rgb "black" linewidth 2

unset multiplot

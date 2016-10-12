#!/bin/bash

arr=`ls  TPhoto*.jpg`
x=0
for photo in $arr
do
((x=x+1))
mv $photo "input$x.jpg"
done

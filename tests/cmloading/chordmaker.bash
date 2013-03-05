#!/bin/bash
awk 'BEGIN { for (i = 1; i <= 4; i++)
printf("1/4, %d %d %d\n", int(rand()*12), int(rand()*12), int(rand()*12))}'

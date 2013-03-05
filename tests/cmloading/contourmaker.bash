#!/bin/bash
awk 'BEGIN { srand();
for (i = 1; i <= 8; i++)
printf("1/8, %f\n", rand())}'

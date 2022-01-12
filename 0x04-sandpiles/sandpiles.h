
#ifndef SANDPILES_H_
#define SANDPILES_H_

#include <stdlib.h>
#include <stdio.h>

void sandpiles_sum(int grid1[3][3], int grid2[3][3]);
void print_grid_unstable(int grid[3][3]);
int sandpiles_check(int grid1[3][3], int grid[3][3]);
void redistribution_sand(int grid1[3][3], int i, int j);

#endif /* SANDPILES_H_ */
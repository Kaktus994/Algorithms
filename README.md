# Algorithms

<b>Partition function Q:</b>

#

Q(n) gives the number of ways of writting an integer n as a sum of positive integers. More info on the following link: https://mathworld.wolfram.com/PartitionFunctionQ.html
This alghoritm does not take into account "trivial partitionig" i.e. n itself is not considered a partition.
Return: number of partitions (int)
#

<b>Path Sizes</b>

#
Algorithm finds all independent "paths" inside the given matrix(input). NOTE: only matrix(list of lists) is a valid input, also each row has to be the same width.
Path is built out of "1"s and "0" is considered to be the end of the path. "1" is appended to the current path if its  position is either "left", "right", "top", "bottom" of the current node("1"). Diagonals do not count! Adjacent nodes to the current node are called "neighbours"
Return: list of independent path sizes (list)

from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

a = 6
b = 3
if rank == 0:
        c = a + b
        sys.stdout.write("%d\n" % c)
if rank == 1:
        c = a * b
        sys.stdout.write("%d\n" % c)
if rank == 2:
        c = max(a, b)
        sys.stdout.write("%d\n" % c)

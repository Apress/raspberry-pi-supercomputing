from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank % 2 == 0:
    sys.stdout.write("Hello!\n")
else:
    sys.stdout.write("Goodbye!\n")

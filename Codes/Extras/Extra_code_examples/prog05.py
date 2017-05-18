from mpi4py import MPI
import numpy
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# automatic MPI datatype discovery
if rank == 0:
    data = numpy.arange(100, dtype=numpy.float64)
    comm.Send(data, dest=1, tag=13)
    sys.stdout.write("Sent a numpy array from Rank 0!\n")
elif rank == 1:
    data = numpy.empty(100, dtype=numpy.float64)
    comm.Recv(data, source=0, tag=13)
    sys.stdout.write("Received a numpy array at Rank 1!\n")

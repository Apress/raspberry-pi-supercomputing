from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    req = comm.isend(data, dest=1, tag=11)
    sys.stdout.write("Send %f and %f from rank 0.\n" % (data['a'], data['b']))
    req.wait()
elif rank == 1:
    req = comm.irecv(source=0, tag=11)
    data = req.wait()
    sys.stdout.write("Received %f and %f at rank 1.\n" %
                     (data['a'], data['b']))

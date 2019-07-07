from NiaPy.algorithms.basic import GeneticAlgorithm
from NiaPy.algorithms.basic.ga import MutationUros, CrossoverUros
from NiaPy.task.task import StoppingTask, OptimizationType
from NiaPy.benchmarks import Sphere


from NiaPy.benchmarks import Benchmark
from MPDA_decode.instance import Instance

class mpda_benchmark(Benchmark):
    Name = ["mpda_benchmark"]

    def __init__(self, Lower=3, Upper=4):
        r"""Initialize Sphere benchmark.

        Args:
            Lower (Optional[float]): Lower bound of problem.
            Upper (Optional[float]): Upper bound of problem.

        See Also:
            :func:`NiaPy.benchmarks.Benchmark.__init__`

        """

        Benchmark.__init__(self, Lower, Upper)

    @staticmethod
    def latex_code():
        """Return the latex code of the problem.

        Returns:
            [str] -- latex code.

        """

        return r"""$f(\mathbf{x}) = \sum_{i=1}^D x_i^2$"""

    @classmethod
    def function(cls):
        """Return benchmark evaluation function.

        Returns:
            [fun] -- Evaluation function.

        """

        def evaluate(D, sol):

            val = 0.0

            for i in range(D):
                val += sol[i] ** 2

            return val

        return evaluate



for i in range(5):
	task = StoppingTask(D=10, nFES=4000, optType=OptimizationType.MINIMIZATION, benchmark=Sphere())
	algo = GeneticAlgorithm(NP=100, Crossover=CrossoverUros, Mutation=MutationUros, Cr=0.45, Mr=0.9)
	best = algo.run(task=task)
	print('%s -> %s' % (best[0].x, best[1]))

if __name__ == '__main__':
    insName = '14_14_ECCENTRIC_RANDOMCLUSTERED_SVLCV_LVLCV_thre0.1MPDAins.dat'
    ins = Instance('.\\benchmark\\' + insName)
    print(ins)


    raise  Exception("wtf= = wtf")
    ins  = Instance()
    mpda_task = StoppingTask()

# we will run Fireworks Algorithm for 5 independent runs

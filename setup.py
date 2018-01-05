from setuptools import setup

setup(
  name='gym-ai-safety-gridworlds',
    version='0.1',
    description='An unofficial OpenAI Gym interface for DeepMind ai-safety-gridworlds',
    long_description = (
      'This project provides an OpenAI Gym interface for the ai-safety-gridworlds '
      'of DeepMind. OpenAI Gym has become a standard interface to a collection of '
      'environments for reinforcement learning (RL). By providing a Gym interface, '
      'this project helps researchers in the field of AI safety to compare RL '
      'algorithms (including existing implementations such as OpenAI Baselines) '
      'on DeepMind ai-safety-gridworlds.'), 

    url='http://github.com/n0p2/gym-ai-safety-gridworlds',
    author='n0p2',
    author_email='N/A',
    license='Apache 2.0',
    packages=['gym_ai_safety_gridworlds'],

    install_requires=[
      'gym',
      'enum34',       # required by ai-safety-gridworlds 
      'abseil-py',    # required by ai-safety-gridworlds 
      'pycolab',      # required by ai-safety-gridworlds 
      'ai-safety-gridworlds' 
    ],

    dependency_links=[
      'https://github.com/abseil/abseil-py/tarball/master#egg=abseil-py-0.1.7', 
      'https://github.com/deepmind/pycolab/tarball/master#egg=pycolab-0.1',
      'https://github.com/deepmind/ai-safety-gridworlds/tarball/master#egg=ai-safety-gridworlds-0.1'
    ],

    classifiers=[
      'Environment :: Console',
      'Environment :: Console :: Curses',
      'Intended Audience :: Education',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: Apache Software License',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX',
      'Operating System :: Unix',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.6',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Software Development :: Libraries',
    ],

    keywords=(
      'ai '
      'gridworld '
      'gym '
      'reinforcement learning '
    ),
    zip_safe=True
)

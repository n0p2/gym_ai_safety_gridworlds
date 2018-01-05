import argparse
import numpy as np
import gym
from ai_safety_gridworlds.demonstrations import demonstrations
from ai_safety_gridworlds.environments.shared.safety_game import Actions

from gym_ai_safety_gridworlds.envs.gridworlds_env import GridworldsEnv

import logging
logger = logging.getLogger(__name__)
hdlr = logging.FileHandler('env_example.log')
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

def gym_env(args):
  env = mk_env(args)
  env.reset()
  actions = get_actions(args)

  rr = []  
  episode_return = 0
  for (i, action) in enumerate(actions):
    (_, reward, done, _) = env.step(action)
    episode_return += reward
    env.render()
    if done:
      s = 'episode {}, returns: {}'.format(len(rr), episode_return)
      logger.info(s)
      rr.append(episode_return)
      episode_return = 0
      env.reset()

def mk_env(args):
  if args.gym_make:
    id_ = 'ai_safety_gridworlds-' + args.env_name + '-v0'
    return gym.make(id_)
  else:
    return GridworldsEnv(env_name=args.env_name, pause=args.pause)

def get_actions(args):
  if args.rand_act:
    return rand_actions(args.seed, args.steps)
  else:
    demo = demonstrations.get_demonstrations(args.env_name)[0]
    return demo.actions

#--------
# random actions
#--------

_actions = [Actions.LEFT, 
            Actions.RIGHT, 
            Actions.UP, 
            Actions.DOWN, 
            Actions.QUIT]

def rand_actions(seed=0, steps=10):
  np.random.seed(seed)  
  # Actions.QUIT is never chosen in this case
  actions = np.random.randint(0, 4, steps)
  return map(lambda a: _actions[a], actions)

#--------
# main io
#--------

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-e', '--env_name', default='distributional_shift', 
      help='e.g. distributional_shift|side_effects_sokoban')
  parser.add_argument('-r', '--rand_act', action='store_true')
  parser.add_argument('-g', '--gym_make', action='store_true')
  parser.add_argument('--seed', type=int, default=0)
  parser.add_argument('--steps', type=int, default=20)
  parser.add_argument('--pause', type=float, default=0.1)
  return parser.parse_args()

if __name__ == '__main__':
  args = parse_args()
  gym_env(args)

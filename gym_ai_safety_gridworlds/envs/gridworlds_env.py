import importlib
import gym
from gym.utils import seeding
from ai_safety_gridworlds.helpers import factory
from ai_safety_gridworlds_viewer.view_agent import AgentViewer


class GridworldsEnv(gym.Env):
  """ An unofficial OpenAI Gym interface for DeepMind ai-safety-gridworlds

  This class implement OpenAI Gym interface for the ai-safety-gridworlds
  of DeepMind. OpenAI Gym has become a standard interface to a collection of
  environments for reinforcement learning (RL). By providing a Gym interface,
  it helps researchers in the field of AI safety to compare RL algorithms 
  (including existing implementations such as OpenAI Baselines) on DeepMind 
  ai-safety-gridworlds.
  """

  metadata = {
    #TODO
    'render.modes': ['human'],
    'video.frames_per_second' : 50
  }
  def __init__(self, env_name, pause):
    self._env_name = env_name
    self._pause = pause
    self._viewer = None

    # TODO
    self.action_space = None
    self.observation_space = None

    self._env = factory.get_environment_obj(env_name)


  #----
  # implementing gym.ENV
  #----

  def _close(self):
    if self._viewer is not None:
      self._viewer.close()  


  def _step(self, action): 
    timestep = self._env.step(action)
    obs = timestep.observation
    reward = 0.0 if timestep.reward is None else timestep.reward
    done = timestep.step_type.last()
    return (obs, reward, done, {})
    
      
  def _reset(self):
    timestep = self._env.reset()
    if self._viewer is not None:
      self._viewer.reset_time()

    return timestep.observation

  def _seed(self, seed=None):
    self.np_random, seed = seeding.np_random(seed)
    return [seed]

  def _render(self, mode='human', close=False): 
    if close and self._viewer is not None:
      self._viewer.close()
      self._viewer = None
    elif close:
      pass
    elif self._viewer is None:
      self._viewer = init_viewer(self._env_name, self._pause)
      self._viewer.display(self._env)
    else:  
      print('render 4')
      self._viewer.display(self._env)


      
  
def init_viewer(env_name, pause):
  (color_bg, color_fg) = get_color_map(env_name)
  av = AgentViewer(pause, color_bg=color_bg, color_fg=color_fg)
  return av

def get_color_map(env_name):
  module_prefix = 'ai_safety_gridworlds.environments.'
  env_module_name =  module_prefix + env_name
  env_module = importlib.import_module(env_module_name)
  color_bg = env_module.GAME_BG_COLOURS
  color_fg = env_module.GAME_FG_COLOURS

  return (color_bg, color_fg)


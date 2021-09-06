from maze import Maze
from reinforce import SarsaTable

def update():
    for ep in range(100):
        #inital observation
        observation = env.reset()
        
        #agent choose action based on observation 
        action = RL.choose_action(str(observation))

        while True:
            #fresh env
            env.render()

            # RL take action and get next observation and reward
            observation_, reward, done  = env.step(action)
            action_ = RL.choose_action(str(observation_))

            RL.learn(str(observation), action, reward, str(observation_), action_)

            #swap observation and action
            observation = observation_
            action = action_

            # break while loop when end of this episode
            if done:
                break

    print("Game Over")
    env.destroy()

if __name__ == '__main__':
    env = Maze()
    RL = SarsaTable(actions=list(range(env.n_actions)))
    env.after(100, update)
    env.mainloop()

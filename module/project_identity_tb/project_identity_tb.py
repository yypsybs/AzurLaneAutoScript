from module.logger import logger
from module.project_identity_tb.assets import PLANNING, FIRST_WEEK, \
    SKIP_ANIMATION
from module.ui.page import page_tb
from module.ui.ui import UI

# 个性： 安静 温柔 热情 任意
target_personality_map = {'busy_fashion_model': 'quiet',
                          'skilled_painter': 'quiet',
                          'popular_musician': 'quiet',
                          'stellar_actor': 'gentle',
                          'talented_cook': 'gentle',
                          'up_and_coming_writer': 'gentle',
                          'amazing_athlete': 'optimistic',
                          'big_shot_businesswoman': 'optimistic',
                          'lively_farm_owner': 'optimistic',
                          'repetitive_everyday': 'any',
                          'shut_in_life': 'any'}

# 属性： 体能 智慧 气质 感知
# 能力： 表现 乐理 细心 想象 运动 实践
# Physical Fitness, Intelligence, Charisma, Perception,
# Performance, Music Theory, Attention to Detail, Imagination, Athletics, Practical Skills,
target_attribute_and_capacity_map = {'busy_fashion_model': [1600, 0, 3000, 0,
                                                            320, 0, 0, 0, 0, 0],
                                     'skilled_painter': [0, 1600, 0, 3000,
                                                         0, 0, 80, 240, 0, 0],
                                     'popular_musician': [0, 0, 0, 4000,
                                                          0, 320, 0, 0, 0, 0],
                                     'stellar_actor': [0, 0, 3000, 1600,
                                                       240, 80, 0, 0, 0, 0],
                                     'talented_cook': [1600, 0, 0, 3000,
                                                       0, 0, 320, 0, 0, 0],
                                     'up_and_coming_writer': [0, 3000, 0, 1600,
                                                              0, 0, 0, 320, 0, 0],
                                     'amazing_athlete': [4000, 0, 0, 0,
                                                         0, 0, 0, 0, 320, 0],
                                     'big_shot_businesswoman': [0, 3000, 1600, 0,
                                                                0, 0, 0, 0, 0, 320],
                                     'lively_farm_owner': [3000, 1600, 0, 0,
                                                           0, 0, 0, 0, 80, 240],
                                     'repetitive_everyday': [1000, 1000, 1000, 1000,
                                                             0, 0, 0, 0, 0, 0],
                                     'shut_in_life': [0, 0, 0, 0,
                                                      0, 0, 0, 0, 0, 0]}


class ProjectIdentityTB(UI):

    def run(self):
        """
        Pages:
            in: page_main
            out: page_main
        """
        logger.info(f"target : {self.config.ProjectIdentityTB_Target}")
        self.ui_ensure(page_tb, skip_first_screenshot=False)
        self.prepare()
        # 进入循环
        # while True:
        #     # 是否结束
        #     if self.finish_loop():
        #         break
        #     # 未结束, 单周处理
        #     self.week_loop()

        return True

    def prepare(self):
        skip_first_screenshot = True
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()
            if self.appear_then_click(PLANNING, offset=(5, 5), interval=3):
                continue
            if self.appear_then_click(SKIP_ANIMATION, offset=(5, 5), interval=3):
                continue
            if self.appear(FIRST_WEEK, offset=(5, 5), interval=3):
                break

    def finish_loop(self):
        return False

    def week_loop(self):
        pass

    def get_current_status(self):
        pass

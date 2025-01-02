import pygame


class Music:
    def __init__(self, sound_file):
        # 初始化Music类并加载音频文件
        # sound_file (str)

        self.sound = None
        pygame.mixer.init()  # 音乐模块初始化
        self.sound_file = sound_file
        self.load_sound()

    def load_sound(self):
        # 加载音频文件
        self.sound = pygame.mixer.Sound(self.sound_file)

    def play_sound(self):
        # 播放音频
        self.sound.play()

    @staticmethod
    def play_background_music(music_file, volume=0.5):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(volume)  # 设置声音大小
        pygame.mixer.music.play(-1)  # -1代表无限循环播放

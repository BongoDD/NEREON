import os
src1 = r'C:\Users\gmavr\OneDrive\LATEST PROJECTS\NEREON GIT\unity\Assets\Scenes\SampleScene.unity'
dst1 = r'C:\Users\gmavr\OneDrive\LATEST PROJECTS\NEREON GIT\unity\Assets\Scenes\LandingScene.unity'
src2 = r'C:\Users\gmavr\OneDrive\LATEST PROJECTS\NEREON GIT\unity\Assets\Scenes\SampleScene.unity.meta'
dst2 = r'C:\Users\gmavr\OneDrive\LATEST PROJECTS\NEREON GIT\unity\Assets\Scenes\LandingScene.unity.meta'
os.rename(src1, dst1)
os.rename(src2, dst2)
print('Renamed successfully')
print('Files in Scenes dir:', os.listdir(r'C:\Users\gmavr\OneDrive\LATEST PROJECTS\NEREON GIT\unity\Assets\Scenes'))

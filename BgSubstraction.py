import cv2
import PoseModule as pm
#from OutputGraph import outputGraph
#from OutputData import outputData


filename = "joce102.mp4"
if filename.endswith(".mp4"):
    print(filename) #do your video process here


    # INITIALIZING STUFF
    cap = cv2.VideoCapture('inputvids/' + filename)
    detector = pm.poseDetector()
    count = 0
    direction = 0
    form = 0
    i = 0
    # Meta.
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_size = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    #frame_list = []


    # Initialize video writer.
    video_output = cv2.VideoWriter('outputvids/' + filename, fourcc, fps, frame_size, isColor=False)

    # Create Bg Subtraction objects
    fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG()
    fgbg2 = cv2.createBackgroundSubtractorMOG2()
    fgbg3 = cv2.bgsegm.createBackgroundSubtractorGMG()
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

    # WORKING WITH MEDIAPIPE
    while cap.isOpened():
        ret, img = cap.read() 
        if not ret:
            print("Null.Frames")
            break
        width  = cap.get(3)  # float `width`
        height = cap.get(4)  # float `height`

        # Apply mask for background subtraction
        fgmask = fgbg3.apply(img)
        #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

        # Mediapipe stuff
        pose = detector.findPose(fgmask, False)
        lmList = detector.findPosition(img, False)
        current_Frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        if len(lmList) != 0: 
            right_hip = detector.findAngle(pose, 12, 24, 26)
            right_knee = detector.findAngle(pose, 24, 26, 28)
            right_ankle = detector.findAngle(pose, 26, 28, 32)
            right_shoulder = detector.findAngle(pose, 14, 12, 24)
            right_elbow = detector.findAngle(pose, 12, 14, 16)

            cv2.putText(pose, str(int(current_Frame)), (25, 60), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 2)


        # This line plays the output video before moving on to the next one
        cv2.imshow('GAIT', pose)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        video_output.write(pose)

    cap.release()
    cv2.destroyAllWindows()
    video_output.release()

    print('finished')
else:
    print('undetected')
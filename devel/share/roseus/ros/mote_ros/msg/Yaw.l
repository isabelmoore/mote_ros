;; Auto-generated. Do not edit!


(when (boundp 'mote_ros::Yaw)
  (if (not (find-package "MOTE_ROS"))
    (make-package "MOTE_ROS"))
  (shadow 'Yaw (find-package "MOTE_ROS")))
(unless (find-package "MOTE_ROS::YAW")
  (make-package "MOTE_ROS::YAW"))

(in-package "ROS")
;;//! \htmlinclude Yaw.msg.html


(defclass mote_ros::Yaw
  :super ros::object
  :slots (_yaw_rad _yaw_rate _yaw_x_position _yaw_y_position ))

(defmethod mote_ros::Yaw
  (:init
   (&key
    ((:yaw_rad __yaw_rad) 0.0)
    ((:yaw_rate __yaw_rate) 0.0)
    ((:yaw_x_position __yaw_x_position) 0.0)
    ((:yaw_y_position __yaw_y_position) 0.0)
    )
   (send-super :init)
   (setq _yaw_rad (float __yaw_rad))
   (setq _yaw_rate (float __yaw_rate))
   (setq _yaw_x_position (float __yaw_x_position))
   (setq _yaw_y_position (float __yaw_y_position))
   self)
  (:yaw_rad
   (&optional __yaw_rad)
   (if __yaw_rad (setq _yaw_rad __yaw_rad)) _yaw_rad)
  (:yaw_rate
   (&optional __yaw_rate)
   (if __yaw_rate (setq _yaw_rate __yaw_rate)) _yaw_rate)
  (:yaw_x_position
   (&optional __yaw_x_position)
   (if __yaw_x_position (setq _yaw_x_position __yaw_x_position)) _yaw_x_position)
  (:yaw_y_position
   (&optional __yaw_y_position)
   (if __yaw_y_position (setq _yaw_y_position __yaw_y_position)) _yaw_y_position)
  (:serialization-length
   ()
   (+
    ;; float64 _yaw_rad
    8
    ;; float64 _yaw_rate
    8
    ;; float64 _yaw_x_position
    8
    ;; float64 _yaw_y_position
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _yaw_rad
       (sys::poke _yaw_rad (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw_rate
       (sys::poke _yaw_rate (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw_x_position
       (sys::poke _yaw_x_position (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw_y_position
       (sys::poke _yaw_y_position (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _yaw_rad
     (setq _yaw_rad (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw_rate
     (setq _yaw_rate (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw_x_position
     (setq _yaw_x_position (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw_y_position
     (setq _yaw_y_position (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get mote_ros::Yaw :md5sum-) "1b1bf6d09d1901c86cf97837e897882f")
(setf (get mote_ros::Yaw :datatype-) "mote_ros/Yaw")
(setf (get mote_ros::Yaw :definition-)
      "float64 yaw_rad
float64 yaw_rate
float64 yaw_x_position
float64 yaw_y_position
")



(provide :mote_ros/Yaw "1b1bf6d09d1901c86cf97837e897882f")



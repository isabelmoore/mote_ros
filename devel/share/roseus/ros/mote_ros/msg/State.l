;; Auto-generated. Do not edit!


(when (boundp 'mote_ros::State)
  (if (not (find-package "MOTE_ROS"))
    (make-package "MOTE_ROS"))
  (shadow 'State (find-package "MOTE_ROS")))
(unless (find-package "MOTE_ROS::STATE")
  (make-package "MOTE_ROS::STATE"))

(in-package "ROS")
;;//! \htmlinclude State.msg.html


(defclass mote_ros::State
  :super ros::object
  :slots (_x_position _y_position _velocity _yaw _yaw_rate ))

(defmethod mote_ros::State
  (:init
   (&key
    ((:x_position __x_position) 0.0)
    ((:y_position __y_position) 0.0)
    ((:velocity __velocity) 0.0)
    ((:yaw __yaw) 0.0)
    ((:yaw_rate __yaw_rate) 0.0)
    )
   (send-super :init)
   (setq _x_position (float __x_position))
   (setq _y_position (float __y_position))
   (setq _velocity (float __velocity))
   (setq _yaw (float __yaw))
   (setq _yaw_rate (float __yaw_rate))
   self)
  (:x_position
   (&optional __x_position)
   (if __x_position (setq _x_position __x_position)) _x_position)
  (:y_position
   (&optional __y_position)
   (if __y_position (setq _y_position __y_position)) _y_position)
  (:velocity
   (&optional __velocity)
   (if __velocity (setq _velocity __velocity)) _velocity)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:yaw_rate
   (&optional __yaw_rate)
   (if __yaw_rate (setq _yaw_rate __yaw_rate)) _yaw_rate)
  (:serialization-length
   ()
   (+
    ;; float64 _x_position
    8
    ;; float64 _y_position
    8
    ;; float64 _velocity
    8
    ;; float64 _yaw
    8
    ;; float64 _yaw_rate
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x_position
       (sys::poke _x_position (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y_position
       (sys::poke _y_position (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _velocity
       (sys::poke _velocity (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw_rate
       (sys::poke _yaw_rate (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x_position
     (setq _x_position (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y_position
     (setq _y_position (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _velocity
     (setq _velocity (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw
     (setq _yaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw_rate
     (setq _yaw_rate (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get mote_ros::State :md5sum-) "bdfa267761e7acb2cdb6844c4c075ccd")
(setf (get mote_ros::State :datatype-) "mote_ros/State")
(setf (get mote_ros::State :definition-)
      "float64 x_position
float64 y_position
float64 velocity
float64 yaw
float64 yaw_rate

")



(provide :mote_ros/State "bdfa267761e7acb2cdb6844c4c075ccd")



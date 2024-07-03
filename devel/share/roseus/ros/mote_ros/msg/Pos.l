;; Auto-generated. Do not edit!


(when (boundp 'mote_ros::Pos)
  (if (not (find-package "MOTE_ROS"))
    (make-package "MOTE_ROS"))
  (shadow 'Pos (find-package "MOTE_ROS")))
(unless (find-package "MOTE_ROS::POS")
  (make-package "MOTE_ROS::POS"))

(in-package "ROS")
;;//! \htmlinclude Pos.msg.html


(defclass mote_ros::Pos
  :super ros::object
  :slots (_act_x_pos _act_y_pos _true_x_pos _true_y_pos _traj_x_pos _traj_y_pos ))

(defmethod mote_ros::Pos
  (:init
   (&key
    ((:act_x_pos __act_x_pos) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:act_y_pos __act_y_pos) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:true_x_pos __true_x_pos) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:true_y_pos __true_y_pos) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:traj_x_pos __traj_x_pos) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:traj_y_pos __traj_y_pos) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _act_x_pos __act_x_pos)
   (setq _act_y_pos __act_y_pos)
   (setq _true_x_pos __true_x_pos)
   (setq _true_y_pos __true_y_pos)
   (setq _traj_x_pos __traj_x_pos)
   (setq _traj_y_pos __traj_y_pos)
   self)
  (:act_x_pos
   (&optional __act_x_pos)
   (if __act_x_pos (setq _act_x_pos __act_x_pos)) _act_x_pos)
  (:act_y_pos
   (&optional __act_y_pos)
   (if __act_y_pos (setq _act_y_pos __act_y_pos)) _act_y_pos)
  (:true_x_pos
   (&optional __true_x_pos)
   (if __true_x_pos (setq _true_x_pos __true_x_pos)) _true_x_pos)
  (:true_y_pos
   (&optional __true_y_pos)
   (if __true_y_pos (setq _true_y_pos __true_y_pos)) _true_y_pos)
  (:traj_x_pos
   (&optional __traj_x_pos)
   (if __traj_x_pos (setq _traj_x_pos __traj_x_pos)) _traj_x_pos)
  (:traj_y_pos
   (&optional __traj_y_pos)
   (if __traj_y_pos (setq _traj_y_pos __traj_y_pos)) _traj_y_pos)
  (:serialization-length
   ()
   (+
    ;; float64[] _act_x_pos
    (* 8    (length _act_x_pos)) 4
    ;; float64[] _act_y_pos
    (* 8    (length _act_y_pos)) 4
    ;; float64[] _true_x_pos
    (* 8    (length _true_x_pos)) 4
    ;; float64[] _true_y_pos
    (* 8    (length _true_y_pos)) 4
    ;; float64[] _traj_x_pos
    (* 8    (length _traj_x_pos)) 4
    ;; float64[] _traj_y_pos
    (* 8    (length _traj_y_pos)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _act_x_pos
     (write-long (length _act_x_pos) s)
     (dotimes (i (length _act_x_pos))
       (sys::poke (elt _act_x_pos i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _act_y_pos
     (write-long (length _act_y_pos) s)
     (dotimes (i (length _act_y_pos))
       (sys::poke (elt _act_y_pos i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _true_x_pos
     (write-long (length _true_x_pos) s)
     (dotimes (i (length _true_x_pos))
       (sys::poke (elt _true_x_pos i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _true_y_pos
     (write-long (length _true_y_pos) s)
     (dotimes (i (length _true_y_pos))
       (sys::poke (elt _true_y_pos i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _traj_x_pos
     (write-long (length _traj_x_pos) s)
     (dotimes (i (length _traj_x_pos))
       (sys::poke (elt _traj_x_pos i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _traj_y_pos
     (write-long (length _traj_y_pos) s)
     (dotimes (i (length _traj_y_pos))
       (sys::poke (elt _traj_y_pos i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _act_x_pos
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _act_x_pos (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _act_x_pos i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _act_y_pos
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _act_y_pos (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _act_y_pos i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _true_x_pos
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _true_x_pos (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _true_x_pos i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _true_y_pos
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _true_y_pos (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _true_y_pos i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _traj_x_pos
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _traj_x_pos (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _traj_x_pos i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _traj_y_pos
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _traj_y_pos (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _traj_y_pos i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get mote_ros::Pos :md5sum-) "7d1a051bd496b12b36f5467e6e2f8b10")
(setf (get mote_ros::Pos :datatype-) "mote_ros/Pos")
(setf (get mote_ros::Pos :definition-)
      "float64[] act_x_pos
float64[] act_y_pos
float64[] true_x_pos
float64[] true_y_pos
float64[] traj_x_pos
float64[] traj_y_pos
")



(provide :mote_ros/Pos "7d1a051bd496b12b36f5467e6e2f8b10")



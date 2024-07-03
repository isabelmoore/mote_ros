; Auto-generated. Do not edit!


(cl:in-package mote_ros-msg)


;//! \htmlinclude Yaw.msg.html

(cl:defclass <Yaw> (roslisp-msg-protocol:ros-message)
  ((yaw_rad
    :reader yaw_rad
    :initarg :yaw_rad
    :type cl:float
    :initform 0.0)
   (yaw_rate
    :reader yaw_rate
    :initarg :yaw_rate
    :type cl:float
    :initform 0.0)
   (yaw_x_position
    :reader yaw_x_position
    :initarg :yaw_x_position
    :type cl:float
    :initform 0.0)
   (yaw_y_position
    :reader yaw_y_position
    :initarg :yaw_y_position
    :type cl:float
    :initform 0.0))
)

(cl:defclass Yaw (<Yaw>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Yaw>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Yaw)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mote_ros-msg:<Yaw> is deprecated: use mote_ros-msg:Yaw instead.")))

(cl:ensure-generic-function 'yaw_rad-val :lambda-list '(m))
(cl:defmethod yaw_rad-val ((m <Yaw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mote_ros-msg:yaw_rad-val is deprecated.  Use mote_ros-msg:yaw_rad instead.")
  (yaw_rad m))

(cl:ensure-generic-function 'yaw_rate-val :lambda-list '(m))
(cl:defmethod yaw_rate-val ((m <Yaw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mote_ros-msg:yaw_rate-val is deprecated.  Use mote_ros-msg:yaw_rate instead.")
  (yaw_rate m))

(cl:ensure-generic-function 'yaw_x_position-val :lambda-list '(m))
(cl:defmethod yaw_x_position-val ((m <Yaw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mote_ros-msg:yaw_x_position-val is deprecated.  Use mote_ros-msg:yaw_x_position instead.")
  (yaw_x_position m))

(cl:ensure-generic-function 'yaw_y_position-val :lambda-list '(m))
(cl:defmethod yaw_y_position-val ((m <Yaw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mote_ros-msg:yaw_y_position-val is deprecated.  Use mote_ros-msg:yaw_y_position instead.")
  (yaw_y_position m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Yaw>) ostream)
  "Serializes a message object of type '<Yaw>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'yaw_rad))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'yaw_rate))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'yaw_x_position))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'yaw_y_position))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Yaw>) istream)
  "Deserializes a message object of type '<Yaw>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yaw_rad) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yaw_rate) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yaw_x_position) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yaw_y_position) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Yaw>)))
  "Returns string type for a message object of type '<Yaw>"
  "mote_ros/Yaw")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Yaw)))
  "Returns string type for a message object of type 'Yaw"
  "mote_ros/Yaw")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Yaw>)))
  "Returns md5sum for a message object of type '<Yaw>"
  "1b1bf6d09d1901c86cf97837e897882f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Yaw)))
  "Returns md5sum for a message object of type 'Yaw"
  "1b1bf6d09d1901c86cf97837e897882f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Yaw>)))
  "Returns full string definition for message of type '<Yaw>"
  (cl:format cl:nil "float64 yaw_rad~%float64 yaw_rate~%float64 yaw_x_position~%float64 yaw_y_position~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Yaw)))
  "Returns full string definition for message of type 'Yaw"
  (cl:format cl:nil "float64 yaw_rad~%float64 yaw_rate~%float64 yaw_x_position~%float64 yaw_y_position~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Yaw>))
  (cl:+ 0
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Yaw>))
  "Converts a ROS message object to a list"
  (cl:list 'Yaw
    (cl:cons ':yaw_rad (yaw_rad msg))
    (cl:cons ':yaw_rate (yaw_rate msg))
    (cl:cons ':yaw_x_position (yaw_x_position msg))
    (cl:cons ':yaw_y_position (yaw_y_position msg))
))

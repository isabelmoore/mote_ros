
(cl:in-package :asdf)

(defsystem "mote_ros-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Pos" :depends-on ("_package_Pos"))
    (:file "_package_Pos" :depends-on ("_package"))
    (:file "State" :depends-on ("_package_State"))
    (:file "_package_State" :depends-on ("_package"))
    (:file "Yaw" :depends-on ("_package_Yaw"))
    (:file "_package_Yaw" :depends-on ("_package"))
  ))
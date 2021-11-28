;; Auto-generated. Do not edit!


(when (boundp 'edrom_tutorial::edrom_message)
  (if (not (find-package "EDROM_TUTORIAL"))
    (make-package "EDROM_TUTORIAL"))
  (shadow 'edrom_message (find-package "EDROM_TUTORIAL")))
(unless (find-package "EDROM_TUTORIAL::EDROM_MESSAGE")
  (make-package "EDROM_TUTORIAL::EDROM_MESSAGE"))

(in-package "ROS")
;;//! \htmlinclude edrom_message.msg.html


(defclass edrom_tutorial::edrom_message
  :super ros::object
  :slots (_str ))

(defmethod edrom_tutorial::edrom_message
  (:init
   (&key
    ((:str __str) "")
    )
   (send-super :init)
   (setq _str (string __str))
   self)
  (:str
   (&optional __str)
   (if __str (setq _str __str)) _str)
  (:serialization-length
   ()
   (+
    ;; string _str
    4 (length _str)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _str
       (write-long (length _str) s) (princ _str s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _str
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _str (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get edrom_tutorial::edrom_message :md5sum-) "994972b6e03928b2476860ce6c4c8e17")
(setf (get edrom_tutorial::edrom_message :datatype-) "edrom_tutorial/edrom_message")
(setf (get edrom_tutorial::edrom_message :definition-)
      "string str

")



(provide :edrom_tutorial/edrom_message "994972b6e03928b2476860ce6c4c8e17")



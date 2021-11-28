; Auto-generated. Do not edit!


(cl:in-package edrom_tutorial-msg)


;//! \htmlinclude edrom_message.msg.html

(cl:defclass <edrom_message> (roslisp-msg-protocol:ros-message)
  ((str
    :reader str
    :initarg :str
    :type cl:string
    :initform ""))
)

(cl:defclass edrom_message (<edrom_message>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <edrom_message>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'edrom_message)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name edrom_tutorial-msg:<edrom_message> is deprecated: use edrom_tutorial-msg:edrom_message instead.")))

(cl:ensure-generic-function 'str-val :lambda-list '(m))
(cl:defmethod str-val ((m <edrom_message>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader edrom_tutorial-msg:str-val is deprecated.  Use edrom_tutorial-msg:str instead.")
  (str m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <edrom_message>) ostream)
  "Serializes a message object of type '<edrom_message>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'str))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'str))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <edrom_message>) istream)
  "Deserializes a message object of type '<edrom_message>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'str) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'str) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<edrom_message>)))
  "Returns string type for a message object of type '<edrom_message>"
  "edrom_tutorial/edrom_message")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'edrom_message)))
  "Returns string type for a message object of type 'edrom_message"
  "edrom_tutorial/edrom_message")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<edrom_message>)))
  "Returns md5sum for a message object of type '<edrom_message>"
  "994972b6e03928b2476860ce6c4c8e17")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'edrom_message)))
  "Returns md5sum for a message object of type 'edrom_message"
  "994972b6e03928b2476860ce6c4c8e17")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<edrom_message>)))
  "Returns full string definition for message of type '<edrom_message>"
  (cl:format cl:nil "string str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'edrom_message)))
  "Returns full string definition for message of type 'edrom_message"
  (cl:format cl:nil "string str~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <edrom_message>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'str))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <edrom_message>))
  "Converts a ROS message object to a list"
  (cl:list 'edrom_message
    (cl:cons ':str (str msg))
))

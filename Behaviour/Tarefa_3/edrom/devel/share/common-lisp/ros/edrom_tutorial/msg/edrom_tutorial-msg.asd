
(cl:in-package :asdf)

(defsystem "edrom_tutorial-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "edrom_message" :depends-on ("_package_edrom_message"))
    (:file "_package_edrom_message" :depends-on ("_package"))
  ))
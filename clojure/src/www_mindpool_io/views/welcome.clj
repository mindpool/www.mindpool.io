(ns www-mindpool-io.views.welcome
  (:require [www-mindpool-io.views.common :as common]
            [noir.content.getting-started])
  (:use [noir.core :only [defpage]]))

(defpage "/welcome" []
         (common/layout
           [:p "Welcome to www-mindpool-io"]))

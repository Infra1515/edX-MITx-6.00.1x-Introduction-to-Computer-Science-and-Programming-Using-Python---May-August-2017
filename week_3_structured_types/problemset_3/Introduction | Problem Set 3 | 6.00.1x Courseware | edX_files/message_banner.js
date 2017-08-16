RequireJS.define("text",{load:function(e){throw new Error("Dynamic load not allowed: "+e)}}),RequireJS.define("text!templates/fields/message_banner.underscore",[],function(){return'<div class="wrapper-msg urgency-<%= urgency %> <%= type %>">\n    <div class="msg">\n        <div class="msg-content">\n            <div class="copy">\n                <p><%-message%></p>\n            </div>\n        </div>\n    </div>\n</div>\n'}),function(e,s){"use strict";RequireJS.define("js/views/message_banner",["gettext","jquery","underscore","backbone","text!templates/fields/message_banner.underscore"],function(e,s,n,i,t){var r=i.View.extend({initialize:function(e){n.isUndefined(e)&&(e={}),this.options=n.defaults(e,{urgency:"high",type:""})},render:function(){return n.isUndefined(this.message)||n.isNull(this.message)?this.$el.html(""):this.$el.html(n.template(t)(n.extend(this.options,{message:this.message}))),this},showMessage:function(e){this.message=e,this.render()},hideMessage:function(){this.message=null,this.render()}});return r})}.call(this,define||RequireJS.define);
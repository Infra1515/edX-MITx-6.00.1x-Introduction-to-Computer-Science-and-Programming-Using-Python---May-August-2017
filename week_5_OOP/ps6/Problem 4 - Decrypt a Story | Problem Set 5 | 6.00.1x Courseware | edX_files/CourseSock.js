!function(e,o){for(var t in o)e[t]=o[t]}(window,webpackJsonp([3],{"./openedx/features/course_experience/static/course_experience/js/CourseSock.js":function(e,o,t){"use strict";Object.defineProperty(o,"__esModule",{value:!0}),function(e){function i(e,o){if(!(e instanceof o))throw new TypeError("Cannot call a class as a function")}t.d(o,"CourseSock",function(){return s});var s=function o(){i(this,o);var t=e(".action-toggle-verification-sock"),s=e(".verification-sock .verification-main-panel"),c=e(".verification-sock .action-upgrade-certificate"),n=window.location.href.indexOf("courseware")>-1?"Course Content Page":"Home Page",a=function(){if(c.is(":visible")){var o=e(window).scrollTop()+e(window).height(),t=s.offset().top+320,i=t+s.height()-220,n=s.offset().left+s.width()-(c.width()+22);o>t&&o<i||e(window).width()<960?(c.addClass("attached"),c.css("left",n+"px")):(c.removeClass("attached"),c.css("left","auto"),o<t?(c.addClass("stuck-top"),c.removeClass("stuck-bottom")):o>i&&(c.addClass("stuck-bottom"),c.removeClass("stuck-top")))}};c.length&&e(window).scroll(a).resize(a),t.on("click",function(){t.toggleClass("active").toggleClass("aria-expanded"),s.slideToggle(400,a);var e=t.hasClass("active"),o=e?"User opened the verification sock.":"User closed the verification sock.";Logger.log(o,{from_page:n})}),c.on("click",function(){Logger.log("User clicked the upgrade button in the verification sock.",{from_page:n})})}}.call(o,t(0))},0:function(e,o){!function(){e.exports=window.jQuery}()}},["./openedx/features/course_experience/static/course_experience/js/CourseSock.js"]));
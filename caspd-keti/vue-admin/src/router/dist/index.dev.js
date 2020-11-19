"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _vue = _interopRequireDefault(require("vue"));

var _vueRouter = _interopRequireDefault(require("vue-router"));

var _Login = _interopRequireDefault(require("../components/login/Login.vue"));

var _Home = _interopRequireDefault(require("../components/home/Home.vue"));

var _HomeMain = _interopRequireDefault(require("../components/home/HomeMain.vue"));

var _Applicant = _interopRequireDefault(require("../components/applicant/Applicant.vue"));

var _Expert = _interopRequireDefault(require("../components/expert/Expert.vue"));

var _ProjectCategory = _interopRequireDefault(require("../components/projectCategory/ProjectCategory.vue"));

var _ProjectAdd = _interopRequireDefault(require("../components/project/ProjectAdd.vue"));

var _ProjectAudit = _interopRequireDefault(require("../components/project/ProjectAudit"));

var _ProjectAssess = _interopRequireDefault(require("../components/project/ProjectAssess.vue"));

var _ProjectDistribute = _interopRequireDefault(require("../components/project/ProjectDistribute"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

_vue["default"].use(_vueRouter["default"]);

var _default = new _vueRouter["default"]({
  routes: [{
    path: '/',
    name: 'login',
    component: _Login["default"]
  }, {
    path: '/home',
    name: 'home',
    component: _Home["default"],
    children: [{
      path: '/',
      name: 'homeMain',
      component: _HomeMain["default"]
    }, {
      path: '/applicant',
      name: 'applicant',
      component: _Applicant["default"]
    }, {
      path: '/expert',
      name: 'expert',
      component: _Expert["default"]
    }, {
      path: '/projectCategory',
      name: 'projectCategory',
      component: _ProjectCategory["default"]
    }, {
      path: '/projectAdd',
      name: 'projectAdd',
      component: _ProjectAdd["default"]
    }, {
      path: '/projectAudit',
      name: 'projectAudit',
      component: _ProjectAudit["default"]
    }, {
      path: '/projectAssess',
      name: 'projectAssess',
      component: _ProjectAssess["default"]
    }, {
      path: '/projectDistribute',
      name: 'projectDistribute',
      component: _ProjectDistribute["default"]
    }]
  }]
});

exports["default"] = _default;
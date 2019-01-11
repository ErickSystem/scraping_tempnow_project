

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _react = require('react');

var _react2 = _interopRequireDefault(_react);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _objectWithoutProperties(obj, keys) { var target = {}; for (var i in obj) { if (keys.indexOf(i) >= 0) continue; if (!Object.prototype.hasOwnProperty.call(obj, i)) continue; target[i] = obj[i]; } return target; }

var SquareIcon = function SquareIcon(_ref) {
  var _ref$width = _ref.width;
  var width = _ref$width === undefined ? 36 : _ref$width;
  var _ref$height = _ref.height;
  var height = _ref$height === undefined ? 36 : _ref$height;
  var _ref$viewBox = _ref.viewBox;
  var viewBox = _ref$viewBox === undefined ? '0 0 24 24' : _ref$viewBox;
  var className = _ref.className;
  //var children = _ref.children;

  var props = _objectWithoutProperties(_ref, ['width', 'height', 'viewBox', 'className', 'children']);

  var classes = 'mdi-icon';
  if (className) classes += ' ' + className;

  return _react2.default.createElement(
    'svg',
    _extends({}, props, { width: width, height: height, viewBox: viewBox, className: classes }),
    _react2.default.createElement('path', { d: "M3,3H21V21H3V3M5,5V19H19V5H5Z"})
  );
};

exports.default = SquareIcon;


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

var _react = require('react');

var _react2 = _interopRequireDefault(_react);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _objectWithoutProperties(obj, keys) { var target = {}; for (var i in obj) { if (keys.indexOf(i) >= 0) continue; if (!Object.prototype.hasOwnProperty.call(obj, i)) continue; target[i] = obj[i]; } return target; }

var QueueIcon = function QueueIcon(_ref) {
  var _ref$width = _ref.width;
  var width = _ref$width === undefined ? 24 : _ref$width;
  var _ref$height = _ref.height;
  var height = _ref$height === undefined ? 24 : _ref$height;
  var _ref$viewBox = _ref.viewBox;
  var viewBox = _ref$viewBox === undefined ? '0 0 100 100' : _ref$viewBox;
  var className = _ref.className;

  var props = _objectWithoutProperties(_ref, ['width', 'height', 'viewBox', 'className', 'children']);

  var classes = 'mdi-icon';
  if (className) classes += ' ' + className;

  return _react2.default.createElement(
    'svg',
    _extends({}, props, { width: width, height: height, viewBox: viewBox, className: classes }),
    _react2.default.createElement('path', { d: "M34.582,60.853c-5.214,0-9.456-4.242-9.456-9.456c0-5.213,4.242-9.456,9.456-9.456c5.214,0,9.456,4.242,9.456,9.456  C44.038,56.61,39.796,60.853,34.582,60.853z M34.582,44.573c-3.762,0-6.823,3.061-6.823,6.823c0,3.763,3.061,6.823,6.823,6.823  c3.763,0,6.824-3.061,6.824-6.823C41.405,47.634,38.344,44.573,34.582,44.573z"}),
    _react2.default.createElement('path', { d:"M50,42.507c-5.214,0-9.456-4.242-9.456-9.456c0-5.214,4.241-9.456,9.456-9.456c5.214,0,9.456,4.242,9.456,9.456  C59.456,38.265,55.214,42.507,50,42.507z M50,26.228c-3.763,0-6.824,3.062-6.824,6.824s3.061,6.823,6.824,6.823  c3.762,0,6.823-3.061,6.823-6.823S53.762,26.228,50,26.228z"}),
    _react2.default.createElement('path', { d:"M65.418,24.163c-5.214,0-9.455-4.242-9.455-9.456c0-5.214,4.241-9.456,9.455-9.456c5.215,0,9.456,4.242,9.456,9.456  C74.874,19.921,70.633,24.163,65.418,24.163z M65.418,7.884c-3.763,0-6.823,3.062-6.823,6.824s3.061,6.823,6.823,6.823  c3.764,0,6.824-3.061,6.824-6.823S69.182,7.884,65.418,7.884z"}),
    _react2.default.createElement('path', { d: "M42.721,94.748H26.442c-0.727,0-1.316-0.589-1.316-1.315v-24.61c0-0.727,0.589-1.316,1.316-1.316  c0.727,0,1.316,0.59,1.316,1.316v23.294h13.647V68.658c0-0.727,0.589-1.316,1.316-1.316c0.727,0,1.316,0.59,1.316,1.316v24.774  C44.038,94.159,43.448,94.748,42.721,94.748z"}),
    _react2.default.createElement('path', { d: "M34.582,65.312c-3.863,0-8.471-1.99-8.666-2.075c-0.666-0.29-0.97-1.065-0.68-1.731c0.291-0.666,1.065-0.973,1.732-0.681  c0.042,0.018,4.305,1.855,7.614,1.855c3.321,0,7.571-1.837,7.614-1.855c0.668-0.29,1.442,0.014,1.732,0.68s-0.014,1.442-0.68,1.732  C43.053,63.322,38.445,65.312,34.582,65.312z"}),
    _react2.default.createElement('path', { d: "M20.797,94.748c-0.727,0-1.316-0.589-1.316-1.315V65.094c0-2.116,0.916-3.233,1.684-3.799  c2.126-1.562,5.314-0.631,5.67-0.52c0.694,0.217,1.081,0.954,0.864,1.648c-0.216,0.692-0.954,1.079-1.645,0.864  c-0.58-0.177-2.437-0.534-3.333,0.13c-0.15,0.111-0.607,0.449-0.607,1.676v28.339C22.113,94.159,21.524,94.748,20.797,94.748z"}),
    _react2.default.createElement('path', { d: "M48.367,94.748c-0.727,0-1.316-0.589-1.316-1.315V65.094c0-1.227-0.458-1.564-0.607-1.676  c-0.896-0.664-2.753-0.306-3.333-0.13c-0.694,0.213-1.43-0.177-1.644-0.869c-0.214-0.692,0.17-1.428,0.863-1.644  c0.357-0.11,3.544-1.043,5.67,0.52c0.768,0.565,1.684,1.683,1.684,3.799v28.339C49.683,94.159,49.093,94.748,48.367,94.748z"}),
    _react2.default.createElement('path', { d: "M73.558,58.045h-5.655c-0.728,0-1.316-0.589-1.316-1.315s0.589-1.316,1.316-1.316h4.34V31.955  c0-0.727,0.589-1.316,1.315-1.316s1.316,0.589,1.316,1.316v24.774C74.874,57.456,74.284,58.045,73.558,58.045z"}),
    _react2.default.createElement('path', { d: "M65.418,28.61c-3.863,0-6.82-1.839-7.014-1.924c-0.667-0.291-0.971-1.066-0.681-1.731c0.29-0.666,1.065-0.973,1.732-0.681  c0.042,0.018,2.653,1.704,5.962,1.704c3.321,0,7.571-1.837,7.613-1.855c0.667-0.29,1.443,0.014,1.733,0.68  c0.29,0.666-0.015,1.442-0.681,1.732C73.891,26.62,69.281,28.61,65.418,28.61z"}),
    _react2.default.createElement('path', { d: "M79.202,58.045c-0.727,0-1.315-0.589-1.315-1.315V28.391c0-1.226-0.458-1.564-0.607-1.676  c-0.896-0.663-2.752-0.306-3.332-0.129c-0.694,0.211-1.432-0.177-1.645-0.869c-0.214-0.693,0.17-1.428,0.862-1.644  c0.356-0.111,3.545-1.043,5.671,0.52c0.768,0.564,1.683,1.682,1.683,3.798v28.339C80.519,57.456,79.93,58.045,79.202,58.045z"}),
    _react2.default.createElement('path', { d: "M58.021,76.25h-5.655c-0.728,0-1.316-0.589-1.316-1.315s0.589-1.316,1.316-1.316h4.34V50.16  c0-0.727,0.589-1.316,1.315-1.316s1.316,0.589,1.316,1.316v24.774C59.337,75.661,58.747,76.25,58.021,76.25z"}),
    _react2.default.createElement('path', { d: "M49.881,46.815c-3.863,0-6.82-1.839-7.014-1.924c-0.667-0.291-0.971-1.066-0.681-1.731c0.29-0.666,1.065-0.973,1.732-0.681  c0.042,0.018,2.653,1.704,5.962,1.704c3.321,0,7.571-1.837,7.613-1.855c0.667-0.29,1.443,0.014,1.733,0.68  c0.29,0.666-0.015,1.442-0.681,1.732C58.354,44.825,53.744,46.815,49.881,46.815z"}),
    _react2.default.createElement('path', { d: "M63.665,76.25c-0.727,0-1.315-0.589-1.315-1.315V46.596c0-1.226-0.458-1.564-0.607-1.676  c-0.896-0.663-2.752-0.306-3.332-0.129c-0.694,0.211-1.432-0.177-1.645-0.869c-0.214-0.693,0.17-1.428,0.862-1.644  c0.356-0.111,3.545-1.043,5.671,0.52c0.768,0.564,1.683,1.682,1.683,3.798v28.339C64.981,75.661,64.393,76.25,63.665,76.25z"})
  );
};

exports.default = QueueIcon;
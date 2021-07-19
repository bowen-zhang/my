var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

goog.exportSymbol('proto.my.TestReply', null, global);
goog.exportSymbol('proto.my.TestRequest', null, global);
goog.exportSymbol('proto.my.MyServiceClient', null, global);

const { TestReply, TestRequest } = require('./service_pb.js')
const { MyServiceClient } = require('./service_grpc_web_pb.js');

proto.my.TestReply = TestReply;
proto.my.TestRequest = TestRequest;
proto.my.MyServiceClient = MyServiceClient;

goog.object.extend(exports, proto.my);
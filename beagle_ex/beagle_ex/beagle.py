import rclpy
from rclpy.node import Node
from roboid import *
import roboidai as ai
from my_robot_interfaces.msg import Objectlist
#from .submodules.imported import function

cam = ai.Camera('usb0')


dt = ai.ObjectDetector(multi=True, lang='en')
dt.download_model()
dt.load_model()


class Beagleobject(Node):
    def __init__(self):
        super().__init__("object_node")
        self.publisher_ = self.create_publisher(
            Objectlist, "object_topic",10) #type, topic name, queue size
        self.timer_ = self.create_timer(0.5,self.find_object)
        self.timer_ = self.create_timer(0.5, self.publish_object)
        self.get_logger().info("Camera send Object information")
        self.labellist = []  # labellist를 멤버 변수로 선언

        
    def find_object(self):
        image = cam.read()
        if dt.detect(image):
            image = dt.draw_result(image)
            self.labellist = dt.get_label()
        
        cam.show(image)
        if cam.check_key() == 'esc': print("break")


        
    def publish_object(self):
        msg = Objectlist()
        msg.object_list = [str(label) for label in self.labellist]
        self.publisher_.publish(msg) 
        

        
def main(args=None):
    rclpy.init(args=args)
    node = Beagleobject()
    rclpy.spin(node)
    #function()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
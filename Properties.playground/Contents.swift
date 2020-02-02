import UIKit

struct Customer{
    var age : Int
    
    var fan_age: Int{
        get{
            return age * 7
        }
    }
}

var B = Customer(age: 2)
print(B.fan_age)

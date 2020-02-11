import UIKit

struct Customer{
    var age : Int
    static var favo : String = "favoriets song"
    
    var fan_age: Int{
        get{
            return age * 7
        }
    }
}

var B = Customer(age: 2)
print(B.fan_age)

struct People{
    
    static var favo = "hello there"
    var name: String
    var age : Int
}
let v = People(name: "azizi", age: 25)
print(People.favo)


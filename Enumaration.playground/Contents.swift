import UIKit

enum WeatherType{
    
    case sun
    case wind(speed:Int)
    case snow
    case rain
    
}

// Now we ad

func check_weather(weather:WeatherType) -> String?{
    switch weather {
    case .sun:
        return nil
    case .wind (let speed) where speed < 100:
        return "The speed of wind is less than 100"
    case .wind,.rain:
        return "200"
    case .snow:
        return "snow"
    
    }
}

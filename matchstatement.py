def DisplayErrorCode(n):
   match n:
      case 200: return "Successful Responses"
      case 300: return "Redirection Messages"
      case 400: return "Client Error Responses"
      case 500: return "Server Error Responses"
      case _: return "Invalid Resposne Code"

            "Message contains spam-like patterns",

            "Possible promotional or phishing content"

        ]


    else:


        result = "Safe"


        reasons = [

            "Normal message structure",

            "No suspicious keywords detected",

            "Message appears trustworthy"

        ]



    return render_template(

        "result.html",

        prediction=result,

        confidence=confidence,

        spam_probability=spam_probability,

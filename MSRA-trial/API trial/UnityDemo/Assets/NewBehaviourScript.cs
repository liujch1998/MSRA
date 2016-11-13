using UnityEngine;
using System.Collections;

public class NewBehaviourScript : MonoBehaviour
{
	int width = 64, height = 40;

	void Start ()
	{
		Camera camera = GameObject.FindObjectOfType<Camera> ();
		RenderTexture renderTexture = new RenderTexture (Screen.width, Screen.height, 20);
		camera.targetTexture = renderTexture;
		camera.Render ();
		RenderTexture.active = renderTexture;
		Texture2D screenshot = new Texture2D (width, height, TextureFormat.RGB24, false);
		screenshot.ReadPixels (new Rect (0, 0, width, height), 0, 0);

		byte[] arr = screenshot.EncodeToJPG ();
		string str = "";
		foreach (byte b in arr)
		{
			str += ((int) b).ToString () + " ";

		}
		Debug.Log (str);
		//string str = System.Text.Encoding.Default.GetString (arr);
		//Debug.Log (str[250]);
	}
}

/*using System;
using System.Net.Http.Headers;
using System.Text;
using System.Net.Http;
using System.Web;

public class NewBehaviourScript : MonoBehaviour
{
	void Start ()
	{
		MakeRequest ();
		Console.WriteLine ("Hit ENTER to exit...");
		Console.ReadLine ();
	}

	void MakeRequest ()
	{
		var client = new HttpClient ();
		var queryString = HttpUtility.ParseQueryString (string.Empty);
		
		// Request headers
		client.DefaultRequestHeaders.Add ("Ocp-Apim-Subscription-Key", "{subscription key}");
		
		// Request parameters
		queryString["returnFaceId"] = "true";
		queryString["returnFaceLandmarks"] = "false";
		queryString["returnFaceAttributes"] = "{string}";
		var uri = "https://api.projectoxford.ai/face/v1.0/detect?" + queryString;
		
		HttpResponseMessage response;
		
		// Request body
		byte[] byteData = Encoding.UTF8.GetBytes("{body}");
		
		using (var content = new ByteArrayContent(byteData))
		{
			content.Headers.ContentType = new MediaTypeHeaderValue("< your content type, i.e. application/json >");
			response = await client.PostAsync(uri, content);
		}
		
	}
}
*/


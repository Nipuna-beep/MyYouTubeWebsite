from django.shortcuts import render
import google.generativeai as genai

# ඔබේ API Key එක මෙහි ඇතුළත් කරන්න
genai.configure(api_key="ඔබේ_API_KEY_එක_මෙතනට_දමන්න")

def home(request):
    # Session එකේ චැට් හිස්ට්‍රියක් නැතිනම් අලුතින් එකක් සාදන්න
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        if user_input:
            try:
                # Gemini AI එකෙන් පිළිතුරක් ලබා ගැනීම
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(user_input)
                ai_msg = response.text
                
                # අලුත් පණිවිඩ ලිස්ට් එකට එකතු කිරීම
                updated_history = request.session['chat_history']
                updated_history.append({'user_msg': user_input, 'ai_msg': ai_msg})
                
                # Session එක Update කිරීම
                request.session['chat_history'] = updated_history
                request.session.modified = True
                
            except Exception as e:
                print(f"Error: {e}")

    return render(request, 'home.html', {'chat_history': request.session['chat_history']})
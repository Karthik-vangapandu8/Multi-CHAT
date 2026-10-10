css = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Base App Background - Matte Obsidian & Charcoal Dark */
.stApp {
    background: linear-gradient(135deg, #09090b 0%, #121215 50%, #08080a 100%) !important;
    color: #f4f4f5 !important;
}

/* Header Styling */
header[data-testid="stHeader"] {
    background: rgba(9, 9, 11, 0.8) !important;
    backdrop-filter: blur(12px);
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: #0d0d11 !important;
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(249, 115, 22, 0.2) !important;
}

/* App Title Header Banner */
.main-header {
    background: linear-gradient(135deg, rgba(249, 115, 22, 0.12) 0%, rgba(234, 88, 12, 0.05) 100%);
    border: 1px solid rgba(249, 115, 22, 0.35);
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 10px 30px -10px rgba(249, 115, 22, 0.25);
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.main-title {
    font-size: 1.9rem;
    font-weight: 800;
    background: linear-gradient(135deg, #ff8c00 0%, #f97316 50%, #fb923c 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 12px;
}

/* Status Badges */
.status-badge {
    padding: 6px 16px;
    border-radius: 9999px;
    font-size: 0.825rem;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    letter-spacing: 0.02em;
}

.status-badge.ready {
    background: rgba(34, 197, 94, 0.15);
    color: #4ade80;
    border: 1px solid rgba(34, 197, 94, 0.4);
    box-shadow: 0 0 12px rgba(34, 197, 94, 0.2);
}

.status-badge.waiting {
    background: rgba(249, 115, 22, 0.15);
    color: #fb923c;
    border: 1px solid rgba(249, 115, 22, 0.4);
    box-shadow: 0 0 12px rgba(249, 115, 22, 0.2);
}

/* Chat Container */
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    margin-bottom: 2rem;
}

/* Chat Messages */
.chat-message {
    display: flex;
    gap: 1rem;
    padding: 1.25rem 1.5rem;
    border-radius: 16px;
    animation: slideUp 0.3s ease-out forwards;
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.4);
    line-height: 1.6;
}

@keyframes slideUp {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.chat-message.user {
    background: linear-gradient(135deg, #18181b 0%, #27272a 100%);
    border: 1px solid rgba(255, 255, 255, 0.12);
    margin-left: 2rem;
}

.chat-message.bot {
    background: linear-gradient(135deg, #141417 0%, #1f1a17 100%);
    border: 1px solid rgba(249, 115, 22, 0.35);
    margin-right: 2rem;
    box-shadow: 0 4px 20px rgba(249, 115, 22, 0.12);
}

.chat-message .avatar-box {
    width: 44px;
    height: 44px;
    min-width: 44px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);
}

.chat-message.user .avatar-box {
    background: linear-gradient(135deg, #3f3f46, #27272a);
    color: #f4f4f5;
    border: 1px solid rgba(255, 255, 255, 0.15);
}

.chat-message.bot .avatar-box {
    background: linear-gradient(135deg, #ff6b00, #ea580c);
    color: white;
    box-shadow: 0 0 15px rgba(249, 115, 22, 0.4);
}

.chat-message .message-content {
    flex: 1;
    color: #f4f4f5;
    font-size: 0.975rem;
}

.chat-message .message-author {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 6px;
}

.chat-message.user .message-author {
    color: #a1a1aa;
}

.chat-message.bot .message-author {
    color: #fb923c;
}

/* Primary Button - Orange Gradient */
div.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #ff6b00 0%, #ea580c 100%) !important;
    color: #ffffff !important;
    border: none !important;
    padding: 0.7rem 1.25rem !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    letter-spacing: 0.03em !important;
    transition: all 0.25s ease-in-out !important;
    box-shadow: 0 4px 18px rgba(249, 115, 22, 0.35) !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(249, 115, 22, 0.55) !important;
    background: linear-gradient(135deg, #ff7b1a 0%, #f97316 100%) !important;
}

/* Upload Container */
div[data-testid="stFileUploader"] {
    background: #141417 !important;
    border: 1px dashed rgba(249, 115, 22, 0.3) !important;
    border-radius: 12px !important;
    padding: 0.75rem !important;
}

div[data-testid="stFileUploader"]:hover {
    border-color: rgba(249, 115, 22, 0.6) !important;
}

/* Input Fields styling */
div[data-baseweb="input"] {
    background-color: #141417 !important;
    border-color: rgba(249, 115, 22, 0.3) !important;
    border-radius: 12px !important;
    color: #f4f4f5 !important;
}

div[data-baseweb="input"]:focus-within {
    border-color: #f97316 !important;
    box-shadow: 0 0 12px rgba(249, 115, 22, 0.3) !important;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: #09090b;
}
::-webkit-scrollbar-thumb {
    background: #27272a;
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
    background: #f97316;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar-box">🤖</div>
    <div class="message-content">
        <div class="message-author">PDF Assistant</div>
        <div>{{MSG}}</div>
    </div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar-box">👤</div>
    <div class="message-content">
        <div class="message-author">You</div>
        <div>{{MSG}}</div>
    </div>
</div>
'''

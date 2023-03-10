import pygame
import random
from pygame.locals import *
import time

pygame.init()

#SCREEN
screen_width = 630
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Button Demo')

font = pygame.font.SysFont('Constantia', 30)
questions_font = pygame.font.SysFont('Comicasns', 23)
answers_font = pygame.font.SysFont('Comicsans', 23)
font_topic = pygame.font.SysFont('Arial Black', 20)
font_instruction = pygame.font.SysFont('Arial Black', 20)
#COLORS
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
light_blue = (202, 228, 241)
dark_blue = (52, 78, 91)
green = (0, 255, 0)
hover_col = (75, 225, 255)
click_col = (50, 150, 255)
gray = (192,192,192)
dark_gray = (169,169,169)
clicked = False


class Button():
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = black
    def __init__(self, x, y, text, width, height, button_col, hover_col, click_col):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.button_col = button_col
        self.hover_col = hover_col
        self.click_col = click_col

    def draw(self, screen: pygame.Surface):
        global clicked
        action = False
        pos = pygame.mouse.get_pos()
        button_rect = Rect(self.x, self.y, self.width, self.height)
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        font = pygame.font.SysFont('comicsans', 30)
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action

#DRAW TEXT FUNCTION

def draw_text(text, width, height, screen, font, color):
    draw_text = font.render(text, True, color)
    screen.blit(draw_text, [width, height])

#ENGLISH

#PAUSE
pause = Button(480, 10, 'Pause', 140, 80, red, hover_col, click_col)

#MAIN MENU
resume = Button(230, 30, "Resume", 180, 80, red, hover_col, click_col)
options = Button(230, 150, "Settings", 180, 80, red, hover_col, click_col)
information = Button(230, 270, "Information", 180, 80, red, hover_col, click_col)
quit = Button(230, 510, "Quit", 180, 80, red, hover_col, click_col)


#OPTIONS MENU
audio_settings = Button(210, 30, "Audio settings", 220, 80, red, hover_col, click_col)
video_settings = Button(210, 150, "Video settings", 220, 80, red, hover_col, click_col)
key_bindings = Button(220, 270, "Key bindings", 200, 80, red, hover_col, click_col)
language_button = Button(220, 390, "Language", 200, 80, red, hover_col, click_col)
back = Button(230, 510, "Back", 180, 80, red, hover_col, click_col)

#LANGUAGE OPTIONS
english = Button(230, 30, "English", 180, 80, red, hover_col, click_col)
russian = Button(230, 150, "Russian", 180, 80, red, hover_col, click_col)
german = Button(230, 270, "German", 180, 80, red, hover_col, click_col)
bulgarian = Button(230, 390, "Bulgarian", 180, 80, red, hover_col, click_col)

#GAME

#INTRODUCTION
start_game = Button(100, 450, "Start learning", 400, 80, red, hover_col, click_col)

#topic 1
topic1_button = Button(30, 50, "Topic 1:How to be safe on the internet", 560, 80, red, hover_col, click_col)
next_button = Button(440, 510, "Next", 180, 80, red, hover_col, click_col)
previous_button = Button(10, 510, "Previous", 220, 80, red, hover_col, click_col)
choose_topic_button = Button(20, 510, "Go back to topics", 300, 80, red, hover_col, click_col)
back_to_main_button = Button(40, 510, "Go back to main menu", 540, 80, red, hover_col, click_col)
start_quiz_topic_1 = Button(400, 510, "Start Quiz", 220, 80, red, hover_col, click_col)
next_question_button = Button(400, 510, "Next question", 220, 80, red, hover_col, click_col)
go_back_to_main_button = Button(315, 510, "Back to main menu", 300, 80, red, hover_col, click_col)
quit_button = Button(10, 510, "Quit", 180, 80, red, hover_col, click_col)
next_question_button_after_done = Button(400, 510, "Next question", 220, 80, dark_gray, gray, white)

#topic 2

game_paused = False

subject_1_page = 1

menu = "main"
language = "English"

quiz_data_topic_1 = [
    {
    "question": "What is the main topic of Topic 1?",
    "answers": ["a) How to stay safe in public places", "b) How to stay safe on the internet", "c) How to stay safe in natural disasters", "d) How to stay safe while driving"],
    "correct_answer": "b) How to stay safe on the internet"
    },
    {
    "question": "What is the most important safety measure for child-ren according to Topic 1?",
    "answers": ["a) Cyber security software", "b) Antivirus software", "c) Firewall software", "d) Open communication with parents"],
    "correct_answer": "d) Open communication with parents"
    },
    {
    "question": "What is the main topic of Topic 2?",
    "answers": ["a) How to create a strong password", "b) How to stay safe on social media", "c) How to get the latest anti-virus and firewall software", "d) How to protect your personal information"],
    "correct_answer": "c) How to get the latest anti-virus and firewall software"
    },
    {
    "question": "According to Topic 2, what is the biggest weak spot in internet security?",
    "answers": ["a) Antivirus software", "b) Firewall software", "c) Passwords", "d) Operating systems"],
    "correct_answer": "c) Passwords"
    },
    {
    "question": "What is the main topic of Topic 3?",
    "answers": ["a) How to stay safe while using public Wi-Fi", "b) How to create a strong password ", "c) How to keep personal information private", "d) How to protect against cyber predators"],
    "correct_answer": "b) How to create a strong password"
    },
    {
    "question": "What is the recommended length for a strong passwordaccording to Topic 3?",
    "answers": ["a) 5-8 characters", "b) 8-10 characters", "c) 10-12 characters", "d) at least 15 characters"],
    "correct_answer": "d) at least 15 characters"
    },
    {
    "question": "What is the main topic of Topic 4?",
    "answers": ["a) How to stay safe while traveling", "b) How to keep personal information private", "c) How to stay safe on social media", "d) How to protect against cyber predators"],
    "correct_answer": "b) How to keep personal information private"
    }
]

random.shuffle(quiz_data_topic_1)
run = True

current_question = 0
score = 0

start_time = None

while run:
    
    screen.fill(light_blue)
    if menu == "paused":
        if resume.draw(screen) == True:
            menu = menu_paused_check
        if options.draw(screen) == True:
            menu = "options"
        if information.draw(screen) == True:
            pass
        if quit.draw(screen) == True:
            run = False
    if menu == "options":
        if audio_settings.draw(screen) == True:
            pass
        if video_settings.draw(screen) == True:
            pass
        if key_bindings.draw(screen) == True:
            pass
        if language_button.draw(screen) == True:
            menu = "language"
        if back.draw(screen) == True:
            menu = "paused"        
                
    if menu == "language":
        if english.draw(screen):
            pass
        if russian.draw(screen):
            pass
        if german.draw(screen):
            pass
        if bulgarian.draw(screen):
            pass
        if language == "English":
            if back.draw(screen) == True:
                menu = "options"
    if game_paused == False and menu == "main":
        menu_paused_check = menu
        if pause.draw(screen) == True:
            menu = "paused"

        draw_text("Welcome to our game!", 150, 100, screen, font, black)
        draw_text("In this game you will learn how to protect your", 15, 190, screen, font, black)
        draw_text("data and be safe online.You can choose from 3", 15, 220, screen, font, black)
        draw_text("topics and start learning things about them ", 15, 250, screen, font, black)
        draw_text("and than you can take a quiz to test what you", 15, 280, screen, font, black)
        draw_text("have learned.Enjoy the game!", 15, 310, screen, font, black)

        if start_game.draw(screen) == True:
            menu = "Choose topic"
            pygame.time.delay(500)
        
    if menu == "Choose topic":
        if topic1_button.draw(screen) == True:
            menu = "Topic 1_1"
        if back_to_main_button.draw(screen) == True:
            menu = "main"
        
    if menu == "Topic 1_1":
        if subject_1_page == 1:
            menu_paused_check = menu
            draw_text("How to stay safe on the internet", 120, 50, screen, font_topic, black)
            draw_text("The internet can be a dangerous place for everyone,", 10, 100, screen, font_topic, black) 
            draw_text("but children and teens are especially vulnerable.", 10, 130, screen, font_topic, black)
            draw_text("From cyber predators to social media posts that can ", 10, 160, screen, font_topic, black)
            draw_text("come back to haunt them later in life, online hazards ", 10, 190, screen, font_topic, black)
            draw_text("can have severe, costly, even tragic, consequences.", 10, 220, screen, font_topic, black)
            draw_text("Children may unwittingly expose their families to ", 10, 250, screen, font_topic, black)
            draw_text("internet threats, for example, by accidentally downlo- ", 10, 280, screen, font_topic, black)
            draw_text("ading malware that could give cyber criminals access ", 10, 310, screen, font_topic, black)
            draw_text("to their parents' bank account or other sensitive ", 10, 340, screen, font_topic, black)
            draw_text("information. Although cyber security software can ", 10, 370, screen, font_topic, black)
            draw_text("help protect against some threats,the most important ", 10, 400, screen, font_topic, black)
            draw_text("ant safety measure is open communication with your", 10, 430, screen, font_topic, black)
            draw_text("children.", 10, 460, screen, font_topic, black)
            if pause.draw(screen) == True:
                menu = "paused"
            if next_button.draw(screen) == True:
                menu = "Topic 1_2"
            if choose_topic_button.draw(screen) == True:
                menu = "Choose topic"
    if menu == "Topic 1_2":
        menu_paused_check = menu
        draw_text("1.Get the latest anti-virus and firewall software", 50, 110, screen, font_topic, black)
        draw_text("Internet security software cannot protect against ", 30, 200, screen, font_topic, black)
        draw_text("every threat, but it will detect and remove most mal- ", 30, 230, screen, font_topic, black)
        draw_text("ware—though you should make sure it's to date.", 30, 260, screen, font_topic, black)
        draw_text("Be sure to stay current with your operating system's ", 30, 290, screen, font_topic, black)
        draw_text("updates and updates to applications you use.", 30, 320, screen, font_topic, black)
        draw_text("They provide a vital layer of security.", 30, 350, screen, font_topic, black)
        if pause.draw(screen) == True:
            menu = "paused"
        if next_button.draw(screen) == True:
            menu = "Topic 1_3"
        if previous_button.draw(screen) == True:
            menu = "Topic 1_1"
    if menu == "Topic 1_3":
        menu_paused_check = menu
        draw_text("2.Create a strong and easy-to-remember password", 40, 90, screen, font_topic, black)
        draw_text("Passwords are one of the biggest weak spots in the ", 50, 120, screen, font_topic, black)
        draw_text("whole Internet security structure,but there's currently ", 30, 140, screen, font_topic, black)
        draw_text("no way around them.", 10, 160, screen, font_topic, black)
        draw_text("And the problem with passwords is that people tend to ", 30, 190, screen, font_topic, black)
        draw_text("choose easy ones to remember (such as 'password' ", 30, 220, screen, font_topic, black)
        draw_text("and '123456'),which are also easy for cyber thieves to ", 30, 250, screen, font_topic, black)
        draw_text("guess.Select strong passwords that are harder for ", 30, 280, screen, font_topic, black)
        draw_text("cybercriminals to demystify.Password manager soft- ", 30, 310, screen, font_topic, black)
        draw_text("ware can help you to manage multiple passwords so", 30, 340, screen, font_topic, black)
        draw_text("that you don't forget them.A strong password is one ", 30, 370, screen, font_topic, black)
        draw_text("that is unique and complex—at least 15 characters ", 30, 400, screen, font_topic, black)
        draw_text("long, mixing letters, numbers and special characters.", 30, 430, screen, font_topic, black)
        draw_text("that you don't forget them.", 30, 460, screen, font_topic, black)
        if pause.draw(screen) == True:
            menu = "paused"
        if next_button.draw(screen) == True:
            menu = "Topic 1_4"
        if previous_button.draw(screen) == True:
            menu = "Topic 1_2"
    if menu == "Topic 1_4":
        menu_paused_check = menu
        draw_text("3. Keep Personal Information Professional and Limited", 20, 100, screen, font_topic, black)
        draw_text("Potential employers or customers don't need to know ", 10, 160, screen, font_topic, black)
        draw_text("your personal relationship status or your home address.", 10, 190, screen, font_topic, black)
        draw_text("They do need to know about your expertise and prof- ", 10, 220, screen, font_topic, black)
        draw_text("essional background, and how to get in touch with you.", 10, 250, screen, font_topic, black)
        draw_text("You wouldn't hand purely personal information out to ", 10, 280, screen, font_topic, black)
        draw_text("strangers individually—don't hand it out to millions of ", 10, 310, screen, font_topic, black)
        draw_text("people online.", 10, 340, screen, font_topic, black)
        if pause.draw(screen) == True:
            menu = "paused"
        if next_button.draw(screen) == True:
            menu = "Topic 1_5"
        if previous_button.draw(screen) == True:
            menu = "Topic 1_3"
    if menu == "Topic 1_5":
        menu_paused_check = menu
        draw_text("4. Be Careful What You Download", 20, 100, screen, font_topic, black)
        draw_text("A top goal of cybercriminals is to trick you into down- ", 10, 160, screen, font_topic, black)
        draw_text("loading malware—programs or apps that carry malware ", 10, 190, screen, font_topic, black)
        draw_text("or try to steal information. This malware can be dis- ", 10, 220, screen, font_topic, black)
        draw_text("guised as an app: anything from a popular game to some- ", 10, 250, screen, font_topic, black)
        draw_text("thing that checks traffic or the weather. As PCWorld adv- ", 10, 280, screen, font_topic, black)
        draw_text("ises, don't download apps that look suspicious or come ", 10, 310, screen, font_topic, black)
        draw_text("from a site you don't trust.", 10, 340, screen, font_topic, black)
        if pause.draw(screen) == True:
            menu = "paused"
        if next_button.draw(screen) == True:
            menu = "Topic 1_6"
        if previous_button.draw(screen) == True:
            menu = "Topic 1_4"
    if menu == "Topic 1_6":
        menu_paused_check = menu
        draw_text("5. Be Careful Who You Meet Online", 20, 100, screen, font_topic, black)
        draw_text("People you meet online are not always who they claim to ", 10, 160, screen, font_topic, black)
        draw_text("be. Indeed, they may not even be real. As InfoWorld rep- ", 10, 190, screen, font_topic, black)
        draw_text("orts, fake social media profiles are a popular way for ", 10, 220, screen, font_topic, black)
        draw_text("hackers to cozy up to unwary Web users and pick their ", 10, 250, screen, font_topic, black)
        draw_text("cyber pockets. Be as cautious and sensible in your online ", 10, 280, screen, font_topic, black)
        draw_text("social life as you are in your in-person social life.", 10, 310, screen, font_topic, black)
        if pause.draw(screen) == True:
            menu = "paused"
        if previous_button.draw(screen) == True:
            menu = "Topic 1_5"
        if start_quiz_topic_1.draw(screen) == True:
            menu = "Quiz 1 start"
            start_time = time.time()
            current_question = 0
            score = 0
            skips = 3   
            paused = False
             
    if menu == "Quiz 1 start":   
        menu_paused_check = menu
        screen.fill((light_blue))
        if pause.draw(screen) == True:
            menu = "paused"
            time_started = False
        if skips > 0:
            if next_question_button.draw(screen) == True and current_question + 1 != len(quiz_data_topic_1):
                current_question += 1
                skips -=1
        else:
            if next_question_button_after_done.draw(screen) == True:
                pass
        if len(quiz_data_topic_1[current_question]["question"]) < 70:
            question_text = answers_font.render(quiz_data_topic_1[current_question]["question"], True, black)
            screen.blit(question_text, [10, 130])
        else:
            question_text = quiz_data_topic_1[current_question]["question"]
            first_part = question_text[:52]
            second_part = question_text[52:]
            first_part_text = answers_font.render(first_part, True, black)
            second_part_text = answers_font.render(second_part, True, black)
            screen.blit(first_part_text, [10, 130])
            screen.blit(second_part_text, [10, 160])

                
        for i in range(len(quiz_data_topic_1[current_question]["answers"])):
            answer_text = answers_font.render(quiz_data_topic_1[current_question]["answers"][i], True, black)
            screen.blit(answer_text, [10, 220 + i*50])

        score_text = answers_font.render("Score: {}".format(score), True, black)
        screen.blit(score_text, [50, 500])
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = True
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] <= 400 and game_paused == False:
                    if mouse_pos[1] >= 200 and mouse_pos[1] <= 500 and game_paused == False:

                        answer_index = (mouse_pos[1] - 200) // 50
                            
                        if quiz_data_topic_1[current_question]["answers"][answer_index] == quiz_data_topic_1[current_question]["correct_answer"]:  
                            current_question += 1
                            score += 1
                            start_time = time.time()
                        else:
                            current_question += 1
                            start_time = time.time()
                        if current_question == len(quiz_data_topic_1):
                            menu = "Quiz 1 end"
        if menu != "paused":
            remaining_time = 31 - (time.time() - start_time)
            
            timer_text = answers_font.render(f"Time remaining: {int(remaining_time)}", True, green)
            timer_rect = timer_text.get_rect(center=(300, 50))
            screen.blit(timer_text, timer_rect)
            if remaining_time < 6:
                timer_text = answers_font.render(f"Time remaining: {int(remaining_time)}", True, red)
                timer_rect = timer_text.get_rect(center=(300, 50))
                screen.blit(timer_text, timer_rect)
            if remaining_time <= 0:
                current_question += 1
                start_time = time.time()
        else:
            timer_text = answers_font.render("Paused", True, (0, 0, 0))
            screen.blit(timer_text, timer_rect)            
    if menu == "Quiz 1 end":
        draw_text(f"Your score is: {score}", 200, 300, screen, answers_font, black)
        draw_text("End of the game", 200, 200, screen, answers_font, black)
        if go_back_to_main_button.draw(screen) == True:
            menu = "main"
        if quit_button.draw(screen) == True:
            pygame.quit()
    pygame.display.update()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                game_paused = True
        
    pygame.display.update()
pygame.quit()
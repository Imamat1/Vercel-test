import asyncio
import asyncpg
import os
import uuid
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')

async def create_sample_course():
    """Create a sample course with lessons and tests"""
    
    ssl_context = 'require'
    conn = await asyncpg.connect(DATABASE_URL, ssl=ssl_context)
    
    try:
        # Create sample course
        course_id = str(uuid.uuid4())
        await conn.execute("""
            INSERT INTO courses (
                id, title, slug, description, level, teacher_id, teacher_name, 
                status, difficulty, estimated_duration_hours, lessons_count, 
                tests_count, image_url, "order", created_at, updated_at
            ) VALUES (
                $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16
            )
        """, course_id, 
            "Основы Ислама", 
            "osnovy-islama",
            "Фундаментальный курс для изучения основ исламской веры, включающий изучение столпов Ислама, основных молитв и этики мусульманина.",
            "level_1",
            "teacher-1",
            "Имам Ахмад",
            "published",
            "Начальный",
            8,
            3,
            1,
            "https://images.unsplash.com/photo-1584286595398-a59f21d7e263?w=800&h=400&fit=crop",
            1,
            datetime.utcnow(),
            datetime.utcnow()
        )
        
        # Create lessons
        lessons = [
            {
                "title": "Пять столпов Ислама",
                "content": "Изучение пяти основных столпов Ислама: Шахада (свидетельство веры), Салят (молитва), Закят (обязательная милостыня), Саум (пост в Рамадан), Хадж (паломничество в Мекку).",
                "video_url": "https://www.youtube.com/embed/VgzjhYH7Wys",
                "order": 1
            },
            {
                "title": "Основы молитвы (Салят)",
                "content": "Подробное изучение пяти ежедневных молитв, их времени, правил совершения и духовного значения в жизни мусульманина.",
                "video_url": "https://www.youtube.com/embed/T4auGhmeBlw",
                "order": 2
            },
            {
                "title": "Этика и поведение мусульманина",
                "content": "Изучение исламской этики (Ахлак), правил поведения в обществе, семье и повседневной жизни согласно учению Ислама.",
                "video_url": "https://www.youtube.com/embed/dGGfnLBX3xQ",
                "order": 3
            }
        ]
        
        lesson_ids = []
        for i, lesson in enumerate(lessons):
            lesson_id = str(uuid.uuid4())
            lesson_ids.append(lesson_id)
            
            await conn.execute("""
                INSERT INTO lessons (
                    id, course_id, title, slug, description, content, lesson_type,
                    video_url, "order", is_published, estimated_duration_minutes,
                    created_at, updated_at
                ) VALUES (
                    $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13
                )
            """, lesson_id, course_id, lesson["title"], 
                f"lesson-{i+1}", lesson["title"], lesson["content"], "mixed",
                lesson["video_url"], lesson["order"], True, 30,
                datetime.utcnow(), datetime.utcnow()
            )
        
        # Create tests for each lesson
        test_questions = [
            # Test 1: Пять столпов Ислама
            [
                {
                    "text": "Сколько столпов в Исламе?",
                    "options": ["Три", "Четыре", "Пять", "Шесть"],
                    "correct": "Пять"
                },
                {
                    "text": "Что означает Шахада?",
                    "options": ["Пост", "Молитва", "Свидетельство веры", "Паломничество"],
                    "correct": "Свидетельство веры"
                },
                {
                    "text": "Какой столп Ислама является обязательным для финансово способных мусульман?",
                    "options": ["Салят", "Закят", "Саум", "Хадж"],
                    "correct": "Закят"
                },
                {
                    "text": "В каком месяце мусульмане соблюдают пост?",
                    "options": ["Мухаррам", "Рамадан", "Шавваль", "Раджаб"],
                    "correct": "Рамадан"
                },
                {
                    "text": "Хадж совершается в:",
                    "options": ["Медине", "Мекке", "Иерусалиме", "Кербеле"],
                    "correct": "Мекке"
                }
            ],
            # Test 2: Основы молитвы
            [
                {
                    "text": "Сколько обязательных молитв в день?",
                    "options": ["Три", "Четыре", "Пять", "Шесть"],
                    "correct": "Пять"
                },
                {
                    "text": "Первая утренняя молитва называется:",
                    "options": ["Фаджр", "Зухр", "Аср", "Магриб"],
                    "correct": "Фаджр"
                },
                {
                    "text": "Что необходимо сделать перед молитвой?",
                    "options": ["Поесть", "Омовение (вуду)", "Поспать", "Почитать"],
                    "correct": "Омовение (вуду)"
                },
                {
                    "text": "В какую сторону направляются мусульмане при молитве?",
                    "options": ["На восток", "На запад", "В сторону Каабы", "На север"],
                    "correct": "В сторону Каабы"
                },
                {
                    "text": "Последняя молитва дня называется:",
                    "options": ["Магриб", "Иша", "Аср", "Зухр"],
                    "correct": "Иша"
                }
            ],
            # Test 3: Этика и поведение
            [
                {
                    "text": "Что означает слово 'Ахлак'?",
                    "options": ["Молитва", "Этика и мораль", "Пост", "Паломничество"],
                    "correct": "Этика и мораль"
                },
                {
                    "text": "Какое качество особенно ценится в Исламе?",
                    "options": ["Гордость", "Смирение", "Гнев", "Зависть"],
                    "correct": "Смирение"
                },
                {
                    "text": "Как мусульмане должны относиться к родителям?",
                    "options": ["Равнодушно", "С уважением и почтением", "Критично", "Независимо"],
                    "correct": "С уважением и почтением"
                },
                {
                    "text": "Что запрещено в исламской этике?",
                    "options": ["Честность", "Справедливость", "Ложь", "Милосердие"],
                    "correct": "Ложь"
                },
                {
                    "text": "Какое приветствие используют мусульмане?",
                    "options": ["Привет", "Ас-саляму алейкум", "Добрый день", "Здравствуйте"],
                    "correct": "Ас-саляму алейкум"
                }
            ]
        ]
        
        for i, lesson_id in enumerate(lesson_ids):
            # Create test for this lesson
            test_id = str(uuid.uuid4())
            await conn.execute("""
                INSERT INTO tests (
                    id, title, description, course_id, lesson_id, time_limit_minutes,
                    passing_score, max_attempts, is_published, "order", created_at, updated_at
                ) VALUES (
                    $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12
                )
            """, test_id, 
                f"Тест: {lessons[i]['title']}", 
                f"Проверка знаний по теме '{lessons[i]['title']}'",
                course_id, lesson_id, 10, 70, 3, True, i+1,
                datetime.utcnow(), datetime.utcnow()
            )
            
            # Add questions to test
            for j, question in enumerate(test_questions[i]):
                question_id = str(uuid.uuid4())
                await conn.execute("""
                    INSERT INTO questions (
                        id, test_id, text, question_type, options, correct_answer,
                        explanation, points, "order"
                    ) VALUES (
                        $1, $2, $3, $4, $5, $6, $7, $8, $9
                    )
                """, question_id, test_id, question["text"], "single_choice",
                    question["options"], question["correct"], 
                    "Правильный ответ основан на основах исламского учения.", 1, j+1
                )
        
        # Update course with correct counts
        await conn.execute("""
            UPDATE courses 
            SET lessons_count = 3, tests_count = 3
            WHERE id = $1
        """, course_id)
        
        print(f"✅ Пример курса 'Основы Ислама' создан успешно!")
        print(f"   - ID курса: {course_id}")
        print(f"   - 3 урока с видео контентом")
        print(f"   - 3 теста с 5 вопросами каждый")
        print(f"   - Курс опубликован и доступен студентам")
        
    except Exception as e:
        print(f"❌ Ошибка при создании примера курса: {e}")
        raise
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(create_sample_course())
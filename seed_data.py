import os
from app import app, db
from models import Casino, Review, Tip

def seed_database():
    """Seed the database with initial data"""
    
    # Delete existing data
    Review.query.delete()
    Tip.query.delete()
    Casino.query.delete()
    
    # Create casino entries
    casino_names = [
        'Royal Palace Casino',
        'Golden Nugget',
        'Diamond Club',
        'Lucky Spin',
        'Mega Jackpot'
    ]
    
    casino_data = [
        {
            'name': 'Royal Palace Casino',
            'logo_url': 'https://placehold.co/100x80?text=Royal+Palace',
            'description': 'Luxury casino with a wide variety of games and excellent customer service.',
            'rating': 4.8,
            'bonus_description': 'Welcome bonus: 100% up to $500 + 100 free spins',
            'min_deposit': 10,
            'url': 'https://example.com/royal-palace',
            'is_featured': True,
            'is_new': False
        },
        {
            'name': 'Golden Nugget',
            'logo_url': 'https://placehold.co/100x80?text=Golden+Nugget',
            'description': 'A classic casino experience with hundreds of slot machines and table games.',
            'rating': 4.5,
            'bonus_description': 'Welcome bonus: 200% up to $1000',
            'min_deposit': 20,
            'url': 'https://example.com/golden-nugget',
            'is_featured': True,
            'is_new': False
        },
        {
            'name': 'Diamond Club',
            'logo_url': 'https://placehold.co/100x80?text=Diamond+Club',
            'description': 'Premium casino with exclusive VIP benefits and high-stakes tables.',
            'rating': 4.7,
            'bonus_description': 'VIP Welcome: 150% up to $2000 + 50 free spins',
            'min_deposit': 50,
            'url': 'https://example.com/diamond-club',
            'is_featured': True,
            'is_new': False
        },
        {
            'name': 'Lucky Spin',
            'logo_url': 'https://placehold.co/100x80?text=Lucky+Spin',
            'description': 'Modern casino with innovative games and instant payouts.',
            'rating': 4.3,
            'bonus_description': 'No deposit bonus: 50 free spins',
            'min_deposit': 5,
            'url': 'https://example.com/lucky-spin',
            'is_featured': False,
            'is_new': True
        },
        {
            'name': 'Mega Jackpot',
            'logo_url': 'https://placehold.co/100x80?text=Mega+Jackpot',
            'description': 'Home to the biggest progressive jackpots and daily tournaments.',
            'rating': 4.6,
            'bonus_description': 'Weekly Reload: 50% up to $200',
            'min_deposit': 15,
            'url': 'https://example.com/mega-jackpot',
            'is_featured': False,
            'is_new': True
        }
    ]
    
    # Add casinos and store them for reference
    created_casinos = {}
    for casino_info in casino_data:
        casino = Casino(**casino_info)
        db.session.add(casino)
        db.session.flush()  # This assigns the ID without committing
        created_casinos[casino_info['name']] = casino
    
    # Commit casinos first to ensure IDs are generated
    db.session.commit()
    
    print(f"Created casinos with IDs: {[(name, casino.id) for name, casino in created_casinos.items()]}")
    
    # Create review entries using the actual casino IDs
    reviews = [
        {
            'casino_id': created_casinos['Royal Palace Casino'].id,
            'title': 'Royal Palace Casino Review: Luxury Gaming Experience',
            'content': 'Royal Palace Casino offers an exceptional gaming experience with a wide variety of games including slots, table games, and live dealer options. The customer service is outstanding, and the VIP program provides excellent benefits for loyal players.',
            'pros': 'Great game selection, Fast payouts, Excellent VIP program',
            'cons': 'Higher than average wagering requirements, Limited payment methods'
        },
        {
            'casino_id': created_casinos['Golden Nugget'].id,
            'title': 'Golden Nugget Review: Classic Casino with Modern Touch',
            'content': 'Golden Nugget combines classic casino charm with modern features. Their slot selection is impressive, and the table games have competitive limits for both casual players and high rollers.',
            'pros': 'Huge game library, User-friendly interface, Great mobile experience',
            'cons': 'Customer support can be slow, Some country restrictions'
        }
    ]
    
    for review_data in reviews:
        review = Review(**review_data)
        db.session.add(review)
    
    # Create tip entries
    tips = [
        {
            'title': 'Understanding Casino Bonuses',
            'content': 'Casino bonuses come with terms and conditions that can significantly affect their value. Always read the wagering requirements, game restrictions, and time limits before claiming a bonus.',
            'category': 'Bonuses'
        },
        {
            'title': 'Bankroll Management',
            'content': 'Set a budget before you start playing and stick to it. Divide your bankroll into sessions and never chase losses. Responsible bankroll management is the key to long-term enjoyment.',
            'category': 'Strategy'
        },
        {
            'title': 'Choosing the Right Slots',
            'content': 'Look for slots with high RTP (Return to Player) percentages, typically above 96%. Also consider volatility - low volatility slots pay out small amounts frequently, while high volatility slots pay larger amounts less often.',
            'category': 'Games'
        }
    ]
    
    for tip_data in tips:
        tip = Tip(**tip_data)
        db.session.add(tip)
    
    # Commit changes
    db.session.commit()
    print('Database seeded successfully!')

if __name__ == '__main__':
    with app.app_context():
        seed_database()
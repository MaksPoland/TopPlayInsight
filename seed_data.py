import os
from app import app, db
from models import Casino, Review, Tip

def seed_database():
    """Seed the database with initial data"""
    
    # Delete existing data
    Casino.query.delete()
    Review.query.delete()
    Tip.query.delete()
    
    # Create casino entries
    casinos = [
        {
            'name': 'Spin Casino',
            'logo_url': 'images/spin-casino.svg',
            'description': 'Spin Casino delivers a premium gaming experience with a vast selection of UKGC-licensed games. Their robust security measures ensure a safe environment for UK players, backed by Microgaming's software excellence and eCOGRA certification for fair play.',
            'rating': 4.8,
            'bonus_description': 'Welcome bonus: 100% up to £200 + 50 free spins',
            'min_deposit': 10,
            'url': 'https://www.spincasino.com/uk/',
            'is_featured': True,
            'is_new': False
        },
        {
            'name': 'JackpotCity',
            'logo_url': 'images/jackpotcity-casino.svg',
            'description': 'JackpotCity offers UK players an outstanding online gaming destination with comprehensive UKGC licensing. Their exceptional mobile platform delivers seamless play across devices, with strong encryption technology protecting all transactions and personal data.',
            'rating': 4.7,
            'bonus_description': 'Welcome bonus: 100% up to £300',
            'min_deposit': 10,
            'url': 'https://www.jackpotcitycasino.com/uk/',
            'is_featured': True,
            'is_new': False
        },
        {
            'name': 'Ruby Fortune',
            'logo_url': 'images/ruby-fortune-casino.svg',
            'description': 'Ruby Fortune stands out with its extensive collection of over 700 UKGC-licensed games, offering UK players both quantity and quality. Their commitment to responsible gaming includes advanced tools for self-exclusion and deposit limits, complemented by 24/7 support.',
            'rating': 4.5,
            'bonus_description': 'Welcome bonus: 100% up to £250 + 25 free spins',
            'min_deposit': 10,
            'url': 'https://www.rubyfortune.com/uk/',
            'is_featured': True,
            'is_new': False
        },
        {
            'name': 'Lucky Nugget',
            'logo_url': 'images/lucky-nugget-casino.svg',
            'description': 'Lucky Nugget brings over two decades of gaming excellence to UK players with full UKGC licensing and compliance. Their game selection balances classic favorites with new releases, all secured by industry-standard encryption and regular independent audits.',
            'rating': 4.3,
            'bonus_description': 'Welcome bonus: 150% up to £200',
            'min_deposit': 10,
            'url': 'https://www.luckynuggetcasino.com/uk/',
            'is_featured': False,
            'is_new': True
        },
        {
            'name': 'Royal Vegas Casino',
            'logo_url': 'images/royal-vegas-casino.svg',
            'description': 'Royal Vegas Casino offers UK players a premium gaming experience with full UKGC compliance. Their platform features advanced security measures and responsible gaming tools, alongside a diverse game selection from industry-leading providers and reliable banking options.',
            'rating': 4.6,
            'bonus_description': 'Welcome bonus: 100% up to £200 + 40 free spins',
            'min_deposit': 10,
            'url': 'https://www.royalvegascasino.com/uk/',
            'is_featured': False,
            'is_new': True
        }
    ]
    
    for casino_data in casinos:
        casino = Casino(**casino_data)
        db.session.add(casino)
    
    # Create review entries
    reviews = [
        {
            'casino_id': 1,  # Spin Casino
            'title': 'Spin Casino Review: Premium Gaming Experience',
            'content': 'Spin Casino offers an exceptional gaming experience for UK players with a comprehensive selection of UKGC-licensed games. The interface is intuitive and user-friendly, making navigation seamless. Their welcome bonus is competitive, and the loyalty program rewards regular players generously.',
            'pros': 'Excellent game variety, Fast withdrawals, Outstanding mobile experience, 24/7 customer support',
            'cons': 'Limited cryptocurrency options, Some withdrawal methods have longer processing times'
        },
        {
            'casino_id': 2,  # JackpotCity
            'title': 'JackpotCity Review: Top-Tier Online Casino',
            'content': 'JackpotCity provides a stellar gaming environment with full UKGC licensing and compliance. Their game library is extensive, covering everything from classic slots to immersive live dealer games. The security measures are robust, ensuring all player data and transactions are protected.',
            'pros': 'Large game selection, Excellent progressive jackpots, Strong encryption standards, Regular promotions',
            'cons': 'Wagering requirements slightly higher than average, Limited sports betting options'
        },
        {
            'casino_id': 3,  # Ruby Fortune
            'title': 'Ruby Fortune Review: Quality Gaming Platform',
            'content': 'Ruby Fortune stands out with its impressive collection of over 700 UKGC-licensed games and commitment to player security. UK players benefit from their advanced platform, which delivers smooth gameplay across all devices. The casino's responsible gaming tools are comprehensive.',
            'pros': 'Vast game library, Excellent security measures, Strong responsible gaming focus, Fast payouts',
            'cons': 'Customer support could be more responsive, Limited payment options'
        },
        {
            'casino_id': 4,  # Lucky Nugget
            'title': 'Lucky Nugget Review: Established Gaming Destination',
            'content': 'Lucky Nugget brings decades of experience to UK players with full UKGC compliance. Their interface balances classic design with modern functionality, making it accessible to players of all experience levels. The welcome bonus offers good value with reasonable wagering requirements.',
            'pros': 'Trusted reputation, Regular promotions, Good game variety, Fair wagering requirements',
            'cons': 'Website design could be more modern, Limited exclusive games'
        },
        {
            'casino_id': 5,  # Royal Vegas Casino
            'title': 'Royal Vegas Casino Review: Premium Gaming Experience',
            'content': 'Royal Vegas Casino provides UK players with a premium gaming environment backed by full UKGC licensing. Their game selection balances quantity with quality, featuring titles from leading providers. The loyalty program offers substantial benefits for regular players.',
            'pros': 'Excellent selection of games, Strong security protocols, Generous loyalty rewards, Good mobile experience',
            'cons': 'Withdrawal processing times could be faster, Limited exclusive promotions'
        }
    ]
    
    for review_data in reviews:
        review = Review(**review_data)
        db.session.add(review)
    
    # Create tip entries
    tips = [
        {
            'title': 'Understanding UK Casino Bonuses',
            'content': 'UK-licensed casino bonuses come with specific terms that must be transparent under UKGC regulations. Always review the full T&Cs, focusing on wagering requirements (typically 30-40x), game contributions (slots usually contribute 100% while table games may contribute only 10-20%), maximum bet limits during bonus play, and time restrictions before claiming an offer.',
            'category': 'Bonuses'
        },
        {
            'title': 'Responsible Bankroll Management',
            'content': 'Establish a strict gaming budget separate from essential funds and track all gambling expenses. Implement a "loss limit" approach—decide in advance the maximum you're willing to lose in a session and stop when reached. Consider using deposit limits available through UKGC-licensed casinos' responsible gaming tools to enforce your budget automatically.',
            'category': 'Strategy'
        },
        {
            'title': 'Maximizing Value from UK Slots',
            'content': 'UK-regulated slots must display their RTP (Return to Player) percentage, typically between 94-98%. Higher RTP slots (96%+) offer better long-term value. Additionally, understand volatility—low volatility slots provide frequent small wins ideal for bonus wagering, while high volatility slots offer larger but less frequent payouts better suited for entertainment value.',
            'category': 'Games'
        },
        {
            'title': 'Utilizing UKGC Casino Protection Tools',
            'content': 'All UKGC-licensed casinos must provide responsible gaming tools including deposit limits, loss limits, session time limits, reality checks, and self-exclusion options. Take advantage of these tools to maintain control over your gaming habits. Licensed UK casinos also offer account history views that help track spending patterns over time.',
            'category': 'Safety'
        },
        {
            'title': 'Understanding Verification Requirements',
            'content': 'UK regulations require casinos to verify player identity before allowing withdrawals. Prepare necessary documents in advance (photo ID, proof of address, payment verification) to avoid delays when requesting payouts. Keep in mind that verification is a protective measure ensuring only legitimate account holders can access funds.',
            'category': 'Banking'
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
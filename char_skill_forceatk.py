import random
#from char_skill_effect import charskilleffect

class SkillForceAttack:

    def __init__(self):
        self.skill_frc_attack_cost = 4
        self.skill_frc_attack_cooldown = 1
        self.skill_frc_attack_cooldown_on = False
        self.skill_next_id = 0
        self.skills_frc_attack = []

    def skill_frc_attack_creation(self, skill_class, skill_name, skill_details):
        skill_id = self.skill_next_id
        skill_info = dict(zip(['skill_desc', 'skill_effect_desc', 'skill_effect', 'skill_roll'], skill_details))
        new_skill = {'id_skill': skill_id, 'class_skill': skill_class, 'name_skill': skill_name, 'info_skill': skill_info}
        self.skills_frc_attack.append(new_skill)
        self.skill_next_id += 1
        return new_skill

    def skill_frc_attack_effect(self):
        pass
    
    def skill_frc_attack_hit(self, attacker, skill_name):
        skill_roll = skill_name['info_skill']['skill_roll']
        skill_value = attacker['att_groups']['ATK']
        skill_damage = skill_roll + skill_value
        skill_effect = skill_name['info_skill']['skill_effect']
        print(f"Dado: {skill_roll} + Atributo atk: {skill_value} = Dano total: {skill_damage}")
        return skill_roll, skill_value, skill_damage, skill_effect

skillfrcatk = SkillForceAttack()

skillfrcatk_fireball = skillfrcatk.skill_frc_attack_creation('Mago', 'Bola de Fogo', ('O mago concentra energia em suas mãos para gerar chamas, então estica seus braços e lança uma bola de fogo em direção ao seu oponente, causando um dano poderoso', 'Se acertado, no início do turno seguinte, o inimigo recebe 1-8 de dano decorrente das queimaduras.', None, random.randint(1, 8)))

skillfrcatk_warhammer = skillfrcatk.skill_frc_attack_creation('Bárbaro', 'Martelo de Guerra', ('O bárbaro empunha sua arma e desfere um golpe brutal de cima para baixo, quebrando defesas.', 'Se acertado, este ataque ignora efeitos de defesa e diminui a armadura do inimigo em 1-8 até o fim do seu próximo turno.', None, random.randint(1, 8)))

skillfrcatk_poisoned_dagger = skillfrcatk.skill_frc_attack_creation('Assassino', 'Adaga Envenenada', ('O assassino desliza sua lâmina desferindo um golpe rápido e letal, infundido com um veneno que enfraquece o oponente.', 'Se acertado, até o final do próximo turno do inimigo, o oponente tem desvantagem em ataques e causa 1-8 de dano reduzido.', None, random.randint(1, 8)))

skillfrcatk_reaper_spirit = skillfrcatk.skill_frc_attack_creation('Necromante', 'Espírito Ceifador', ('O necromante conjura uma entidade sinistra que ceifa almas com sua lâmina gélida, drenando parte da força vital do oponente.', 'Se acertado, metade do dano total é retornado em cura para você.', None, random.randint(1, 8)))

skillfrcatk_death_ray = skillfrcatk.skill_frc_attack_creation('Bruxa', 'Raio da Morte', ('A bruxa levanta o tortuoso dedo indicador e aponta para o oponente, lançando um fino raio carregado de energia necrótica.', 'Após acertado, se a vida total do inimigo for reduzida para menos que o dano total causado por essa habilidade, ele morre instântaneamente.', None, random.randint(1, 8)))

if __name__ == '__main__':
    print(skillfrcatk_death_ray)
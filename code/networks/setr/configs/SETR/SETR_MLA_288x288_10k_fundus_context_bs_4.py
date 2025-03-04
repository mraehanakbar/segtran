_base_ = [
    '../_base_/models/setr_mla.py',
    '../_base_/datasets/pascal_context.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_80k.py'
]
norm_cfg = dict(type='BN', requires_grad=True)
model = dict(
    backbone=dict(img_size=288, pos_embed_interp=True, drop_rate=0.,
                  mla_channels=256, mla_index=(5, 11, 17, 23),norm_cfg=norm_cfg),
    decode_head=dict(img_size=288, mla_channels=256,
                     mlahead_channels=128,norm_cfg=norm_cfg ,num_classes=3),
    auxiliary_head=[
        dict(
            type='VIT_MLA_AUXIHead',
            in_channels=256,
            channels=512,
            in_index=0,
            img_size=288,
            num_classes=3,
            align_corners=False,
            loss_decode=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
        dict(
            type='VIT_MLA_AUXIHead',
            in_channels=256,
            channels=512,
            in_index=1,
            img_size=288,
            num_classes=3,
            align_corners=False,
            loss_decode=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
        dict(
            type='VIT_MLA_AUXIHead',
            in_channels=256,
            channels=512,
            in_index=2,
            img_size=288,
            num_classes=3,
            align_corners=False,
            loss_decode=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
        dict(
            type='VIT_MLA_AUXIHead',
            in_channels=256,
            channels=512,
            in_index=3,
            img_size=288,
            num_classes=3,
            align_corners=False,
            loss_decode=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
    ])

optimizer = dict(lr=0.001, weight_decay=0.0,
                 paramwise_cfg=dict(custom_keys={'head': dict(lr_mult=10.)})
                 )

test_cfg = dict(mode='slide', crop_size=(288, 288), stride=(288, 288))
find_unused_parameters = True
data = dict(samples_per_gpu=2)

_base_ = [
    '../_base_/models/setr_naive_pup.py',
    '../_base_/datasets/pascal_context.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_80k.py'
]
norm_cfg = dict(type='BN', requires_grad=True)
model = dict(
    backbone=dict(img_size=288, align_corners=False,
                  pos_embed_interp=True, drop_rate=0., num_classes=3,norm_cfg=norm_cfg),
    decode_head=dict(img_size=288, align_corners=False, num_conv=2,
                     upsampling_method='bilinear', num_classes=3, conv3x3_conv1x1=False,norm_cfg=norm_cfg),
    auxiliary_head=[dict(
        type='VisionTransformerUpHead',
        in_channels=1024,
        channels=512,
        in_index=9,
        img_size=288,
        embed_dim=1024,
        num_classes=3,
        norm_cfg=norm_cfg,
        num_conv=2,
        upsampling_method='bilinear',
        align_corners=False,
        conv3x3_conv1x1=False,
        loss_decode=dict(
            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
        dict(
        type='VisionTransformerUpHead',
        in_channels=1024,
        channels=512,
        in_index=14,
        img_size=288,
        embed_dim=1024,
        num_classes=3,
        norm_cfg=norm_cfg,
        num_conv=2,
        upsampling_method='bilinear',
        align_corners=False,
        conv3x3_conv1x1=False,
        loss_decode=dict(
            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
        dict(
        type='VisionTransformerUpHead',
        in_channels=1024,
        channels=512,
        in_index=19,
        img_size=288,
        embed_dim=1024,
        num_classes=3,
        norm_cfg=norm_cfg,
        num_conv=2,
        upsampling_method='bilinear',
        align_corners=False,
        conv3x3_conv1x1=False,
        loss_decode=dict(
            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
    ])

optimizer = dict(lr=0.01, weight_decay=0.0,
                 paramwise_cfg=dict(custom_keys={'head': dict(lr_mult=10.)})
                 )

test_cfg = dict(mode='slide', crop_size=(288, 288), stride=(288, 288))
find_unused_parameters = True
